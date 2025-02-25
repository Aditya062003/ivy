# global
import ivy
from ivy.functional.frontends.numpy.func_wrapper import to_ivy_arrays_and_back


# squeeze
@to_ivy_arrays_and_back
def squeeze(
    a,
    axis=None,
):
    return ivy.squeeze(a, axis)


# expand_dims
@to_ivy_arrays_and_back
def expand_dims(
    a,
    axis,
):
    return ivy.expand_dims(a, axis=axis)


def atleast_2d(*arys):
    return ivy.atleast_2d(*arys)


def atleast_3d(*arys):
    return ivy.atleast_3d(*arys)
