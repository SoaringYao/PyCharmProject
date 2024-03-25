"""rgb to yuv.

usage: rgb2yuv.py [-hdv] [-f <fmt>] <inp> <out>

options:
    -h, --help
    -d, --debug
    -v, --verbose           print information about image.
    -f, --format <fmt>      Format of yuv. [default: i444]

formats:
    444:
        i444: YYY UUU VVV
        yv24: YYY VVV UUU
        nv24: YYY UV UV UV
        nv42: YYY VU VU VU
    422:
        i422: YYYY UU VV
        yv16: YYYY VV UU
        nv16: YYYY UV UV
        nv61: YYYY VU VU
    420:
        i420: YYYYYYYY UU VV
        yv12: YYYYYYYY UU VV
        nv12: YYYYYYYY UV UV
        nv21: YYYYYYYY VU VU
"""

from typing import TYPE_CHECKING

import torch

# static_checking
if TYPE_CHECKING:
    from torch import Tensor


class YUV4:

    def __init__(self, yuv: "Tensor"):
        self.y, self.u, self.v = yuv.permute(2, 0, 1)
        self.y = self.y.flatten()

    def uuvv(self) -> "Tensor":
        out = torch.cat([self.y, self.u, self.v])
        return out

    def vvuu(self) -> "Tensor":
        out = torch.cat([self.y, self.v, self.u])
        return out

    def uvuv(self) -> "Tensor":
        uv = torch.stack([self.u, self.v], dim=1).flatten()
        out = torch.cat([self.y, uv])
        return out

    def vuvu(self) -> "Tensor":
        uv = torch.stack([self.v, self.u], dim=1).flatten()
        out = torch.cat([self.y, uv])
        return out


class YUV444(YUV4):

    def __init__(self, yuv: "Tensor"):
        super().__init__(yuv)
        self.u = self.u.flatten()
        self.v = self.v.flatten()


class YUV422(YUV4):

    def __init__(self, yuv: "Tensor"):
        super().__init__(yuv)
        self.u = self.u[0::2, :].flatten()
        self.v = self.v[0::2, :].flatten()


class YUV420(YUV4):

    def __init__(self, yuv: "Tensor"):
        super().__init__(yuv)
        self.u = self.u[0::2, 0::2].flatten()
        self.v = self.v[0::2, 0::2].flatten()


class I444(YUV444):

    def __init__(self, yuv: "Tensor"):
        super().__init__(yuv)

    def __call__(self) -> "Tensor":
        return self.uuvv()


class YV24(YUV444):

    def __init__(self, yuv: "Tensor"):
        super().__init__(yuv)

    def __call__(self) -> "Tensor":
        return self.vvuu()


class NV24(YUV444):

    def __init__(self, yuv: "Tensor"):
        super().__init__(yuv)

    def __call__(self) -> "Tensor":
        return self.uvuv()


class NV42(YUV444):

    def __init__(self, yuv: "Tensor"):
        super().__init__(yuv)

    def __call__(self) -> "Tensor":
        return self.vuvu()


class I422(YUV422):

    def __init__(self, yuv: "Tensor"):
        super().__init__(yuv)

    def __call__(self) -> "Tensor":
        return self.uuvv()


class YV16(YUV422):

    def __init__(self, yuv: "Tensor"):
        super().__init__(yuv)

    def __call__(self) -> "Tensor":
        return self.vvuu()


class NV16(YUV422):

    def __init__(self, yuv: "Tensor"):
        super().__init__(yuv)

    def __call__(self) -> "Tensor":
        return self.uvuv()


class NV61(YUV422):

    def __init__(self, yuv: "Tensor"):
        super().__init__(yuv)

    def __call__(self) -> "Tensor":
        return self.vuvu()


class I420(YUV420):

    def __init__(self, yuv: "Tensor"):
        super().__init__(yuv)

    def __call__(self) -> "Tensor":
        return self.uuvv()


class YV12(YUV420):

    def __init__(self, yuv: "Tensor"):
        super().__init__(yuv)

    def __call__(self) -> "Tensor":
        return self.vvuu()


class NV12(YUV420):
    def __init__(self, yuv: "Tensor"):
        super().__init__(yuv)

    def __call__(self) -> "Tensor":
        return self.uvuv()


class NV21(YUV420):

    def __init__(self, yuv: "Tensor"):
        super().__init__(yuv)

    def __call__(self) -> "Tensor":
        return self.vuvu()


YUV_DICT = {
    "i444": I444,
    "yv24": YV24,
    "nv24": NV24,
    "nv42": NV42,
    "i422": I422,
    "yv16": YV16,
    "nv16": NV16,
    "nv61": NV61,
    "i420": I420,
    "yv12": YV12,
    "nv12": NV12,
    "nv21": NV21,
}


def rgb2yuv(rgb: "Tensor") -> "Tensor":
    bt = torch.tensor([[0.299, 0.587, 0.114],
                       [-0.148, -0.289, 0.437],
                       [0.615, -0.515, -0.100], ])
    yuv = rgb @ bt.transpose(1, 0) + torch.tensor([0, 128, 128])
    return yuv


if __name__ == "__main__" and __doc__:
    from docopt import docopt

    args = docopt(__doc__)
    if args["--debug"]:
        print(args)

    from matplotlib.image import imread

    rgb = torch.from_numpy(imread(args["<inp>"]).copy()) + 0.0
    if args["--verbose"]:
        image_size = "x".join(list(map(str, rgb.shape[0:2][::-1])))
        print(f"width*height is {image_size}.")
    yuv = rgb2yuv(rgb)
    yuv = yuv.int().maximum(torch.tensor(0)).minimum(torch.tensor(255))
    if args["--debug"]:
        print(yuv[:, :, 1])
        print(yuv[:, :, 2])
    out = YUV_DICT[args["--format"]](yuv)()
    with open(args["<out>"], mode="wb") as f:
        f.write(bytes(out.tolist()))
