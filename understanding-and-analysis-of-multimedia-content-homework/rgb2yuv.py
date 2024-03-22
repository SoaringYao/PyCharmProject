#! /usr/bin/env python3
# Docstring {{{ #
"""Change rgb to yuv.

usage: rgb2yuv.py [-hVdvn] [-t <tv>] [-f <fmt>] <inp> <out>

options:
    -h, --help              Show this screen.
    -V, --version           Show version.
    -d, --debug             Print debug information.
    -v, --verbose           Print more information.
    -n, --dry-run           Don't output.
    -t, --tv <tv>           TV definition. [default: h]
    -f, --format <fmt>      Format of yuv. [default: i420]

TV definitions:
    s: standard definition.
    h: high definition.

formats:
    444:
        i444: YYYYYYYY UUUUUUUU VVVVVVVV
        yv24: YYYYYYYY VVVVVVVV UUUUUUUU
        nv24: YYYYYYYY UV UV UV UV UV UV UV UV
        nv42: YYYYYYYY VU VU VU VU VU VU VU VU
    422:
        i422: YYYYYYYY UUUU VVVV
        yv16: YYYYYYYY VVVV UUUU
        nv16: YYYYYYYY UV UV UV UV
        nv61: YYYYYYYY VU VU VU VU
    420:
        i420: YYYYYYYY UU VV
        yv12: YYYYYYYY UU VV
        nv12: YYYYYYYY UV UV
        nv21: YYYYYYYY VU VU
"""
# }}} Docstring #
import torch
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from torch import Tensor


# Base Class {{{ #
class YUV4:
    """YUV4."""

    def __init__(self, yuv: "Tensor"):
        """__init__.

        :param yuv:
        :type yuv: "Tensor"
        """
        self.y, self.u, self.v = yuv.permute(2, 0, 1)
        self.y = self.y.flatten()

    def uuvv(self) -> "Tensor":
        """uuvv.

        :rtype: "Tensor"
        """
        out = torch.cat([self.y, self.u, self.v])
        return out

    def vvuu(self) -> "Tensor":
        """vvuu.

        :rtype: "Tensor"
        """
        out = torch.cat([self.y, self.v, self.u])
        return out

    def uvuv(self) -> "Tensor":
        """uvuv.

        :rtype: "Tensor"
        """
        uv = torch.stack([self.u, self.v], dim=1).flatten()
        out = torch.cat([self.y, uv])
        return out

    def vuvu(self) -> "Tensor":
        """vuvu.

        :rtype: "Tensor"
        """
        uv = torch.stack([self.v, self.u], dim=1).flatten()
        out = torch.cat([self.y, uv])
        return out


class YUV444(YUV4):
    """YUV444."""

    def __init__(self, yuv: "Tensor"):
        """__init__.

        :param yuv:
        :type yuv: "Tensor"
        """
        super().__init__(yuv)
        self.u = self.u.flatten()
        self.v = self.v.flatten()


class YUV422(YUV4):
    """YUV422."""

    def __init__(self, yuv: "Tensor"):
        """__init__.

        :param yuv:
        :type yuv: "Tensor"
        """
        super().__init__(yuv)
        self.u = self.u[0::2, :].flatten()
        self.v = self.v[0::2, :].flatten()


class YUV420(YUV4):
    """YUV420."""

    def __init__(self, yuv: "Tensor"):
        """__init__.

        :param yuv:
        :type yuv: "Tensor"
        """
        super().__init__(yuv)
        self.u = self.u[0::2, 0::2].flatten()
        self.v = self.v[0::2, 0::2].flatten()


# }}} Base Class #


# yuv444 {{{ #
class I444(YUV444):
    """I444."""

    def __init__(self, yuv: "Tensor"):
        """__init__.

        :param yuv:
        :type yuv: "Tensor"
        """
        super().__init__(yuv)

    def __call__(self) -> "Tensor":
        """__call__.

        :rtype: "Tensor"
        """
        return self.uuvv()


class YV24(YUV444):
    """YV24."""

    def __init__(self, yuv: "Tensor"):
        """__init__.

        :param yuv:
        :type yuv: "Tensor"
        """
        super().__init__(yuv)

    def __call__(self) -> "Tensor":
        """__call__.

        :rtype: "Tensor"
        """
        return self.vvuu()


class NV24(YUV444):
    """NV24."""

    def __init__(self, yuv: "Tensor"):
        """__init__.

        :param yuv:
        :type yuv: "Tensor"
        """
        super().__init__(yuv)

    def __call__(self) -> "Tensor":
        """__call__.

        :rtype: "Tensor"
        """
        return self.uvuv()


class NV42(YUV444):
    """NV42."""

    def __init__(self, yuv: "Tensor"):
        """__init__.

        :param yuv:
        :type yuv: "Tensor"
        """
        super().__init__(yuv)

    def __call__(self) -> "Tensor":
        """__call__.

        :rtype: "Tensor"
        """
        return self.vuvu()


# }}} yuv444 #


# yuv422 {{{ #
class I422(YUV422):
    """I422."""

    def __init__(self, yuv: "Tensor"):
        """__init__.

        :param yuv:
        :type yuv: "Tensor"
        """
        super().__init__(yuv)

    def __call__(self) -> "Tensor":
        """__call__.

        :rtype: "Tensor"
        """
        return self.uuvv()


class YV16(YUV422):
    """YV16."""

    def __init__(self, yuv: "Tensor"):
        """__init__.

        :param yuv:
        :type yuv: "Tensor"
        """
        super().__init__(yuv)

    def __call__(self) -> "Tensor":
        """__call__.

        :rtype: "Tensor"
        """
        return self.vvuu()


class NV16(YUV422):
    """NV16."""

    def __init__(self, yuv: "Tensor"):
        """__init__.

        :param yuv:
        :type yuv: "Tensor"
        """
        super().__init__(yuv)

    def __call__(self) -> "Tensor":
        """__call__.

        :rtype: "Tensor"
        """
        return self.uvuv()


class NV61(YUV422):
    """NV61."""

    def __init__(self, yuv: "Tensor"):
        """__init__.

        :param yuv:
        :type yuv: "Tensor"
        """
        super().__init__(yuv)

    def __call__(self) -> "Tensor":
        """__call__.

        :rtype: "Tensor"
        """
        return self.vuvu()


# }}} yuv422 #


# yuv420 {{{ #
class I420(YUV420):
    """I420."""

    def __init__(self, yuv: "Tensor"):
        """__init__.

        :param yuv:
        :type yuv: "Tensor"
        """
        super().__init__(yuv)

    def __call__(self) -> "Tensor":
        """__call__.

        :rtype: "Tensor"
        """
        return self.uuvv()


class YV12(YUV420):
    """YV12."""

    def __init__(self, yuv: "Tensor"):
        """__init__.

        :param yuv:
        :type yuv: "Tensor"
        """
        super().__init__(yuv)

    def __call__(self) -> "Tensor":
        """__call__.

        :rtype: "Tensor"
        """
        return self.vvuu()


class NV12(YUV420):
    """NV12."""

    def __init__(self, yuv: "Tensor"):
        """__init__.

        :param yuv:
        :type yuv: "Tensor"
        """
        super().__init__(yuv)

    def __call__(self) -> "Tensor":
        """__call__.

        :rtype: "Tensor"
        """
        return self.uvuv()


class NV21(YUV420):
    """NV21."""

    def __init__(self, yuv: "Tensor"):
        """__init__.

        :param yuv:
        :type yuv: "Tensor"
        """
        super().__init__(yuv)

    def __call__(self) -> "Tensor":
        """__call__.

        :rtype: "Tensor"
        """
        return self.vuvu()


# }}} yuv420 #


# Constant {{{ #
# https://wiki.videolan.org/YUV
YUV_DICT = {
    "i420": I420,
    "yv12": YV12,
    "nv12": NV12,
    "nv21": NV21,
    "i422": I422,
    "yv16": YV16,
    "nv16": NV16,
    "nv61": NV61,
    "i444": I444,
    "yv24": YV24,
    "nv24": NV24,
    "nv42": NV42,
}
# https://en.wikipedia.org/wiki/YUV
BT470 = torch.tensor(
    [
        [0.299, 0.587, 0.114],
        [-0.14713, -0.28886, 0.436],
        [0.615, -0.51499, -0.10001],
    ]
)
BT709 = torch.tensor(
    [
        [0.2126, 0.7152, 0.0722],
        [-0.09991, -0.33609, 0.436],
        [0.615, -0.55861, 0.05639],
    ]
)
BT_DICT = {
    "h": BT470,
    "s": BT709,
}
# }}} Constant #


def rgb2yuv(rgb: "Tensor", bt: "Tensor") -> "Tensor":
    """rgb2yuv.

    :param rgb:
    :type rgb: "Tensor"
    :param bt:
    :type bt: "Tensor"
    :rtype: "Tensor"
    """
    yuv = rgb @ bt.transpose(1, 0) + torch.tensor([0, 128, 128])
    return yuv


if __name__ == "__main__" and __doc__:
    from docopt import docopt

    args = docopt(__doc__, version="0.0.1")
    if args["--debug"]:
        print(args)

    from matplotlib.image import imread

    rgb = torch.from_numpy(imread(args["<inp>"])) + 0.0
    if args["--verbose"]:
        image_size = "x".join(list(map(str, rgb.shape[0:2][::-1])))
        print(f"width*height is {image_size}.")
    yuv = rgb2yuv(rgb, BT_DICT[args["--tv"]])
    yuv = yuv.int().maximum(torch.tensor(0)).minimum(torch.tensor(255))
    if args["--debug"]:
        print(yuv[:, :, 1])
        print(yuv[:, :, 2])
    out = YUV_DICT[args["--format"]](yuv)()
    if args["--dry-run"]:
        exit()
    with open(args["<out>"], mode="wb") as f:
        f.write(bytes(out.tolist()))
# ex: fold-method=marker
