# Built-in modules
from copy import deepcopy
import pickle
# Third-party modules
import numpy as np
from bloscpack import unpack_ndarray_file, pack_ndarray_file
# Hand-made modules
from src.utils.base import PathHandlerBase, concat_dict_key_values


def split_train_validation(ndarray: np.ndarray, begin_val_index, end_val_index):
    if ndarray.ndim == 1:
        return ndarray[:begin_val_index], \
               ndarray[begin_val_index:end_val_index]
    elif ndarray.ndim == 2:
        return ndarray[:begin_val_index, :], \
               ndarray[begin_val_index:end_val_index, :]
    elif ndarray.ndim == 3:
        return ndarray[:begin_val_index, :, :], \
               ndarray[begin_val_index:end_val_index, :, :]
    else:
        raise ValueError("Dimension of input numpy.ndarray must be 1, 2 or 3 !!!")


class BloscpackMixin(object):
    @staticmethod
    def read_blp(path_or_buf):
        return unpack_ndarray_file(path_or_buf)

    @staticmethod
    def to_blp(ndarray: np.ndarray, path_or_buf):
        pack_ndarray_file(ndarray, path_or_buf)


class PickleMixin(object):
    @staticmethod
    def read_pkl(path_or_buf):
        with open(path_or_buf, mode="rb") as f:
            return pickle.load(f)

    @staticmethod
    def to_pkl(obj: object, path_or_buf):
        with open(path_or_buf, mode="wb") as f:
            pickle.dump(obj, f)


class MyEstimatorWrapper(PathHandlerBase, BloscpackMixin, PickleMixin):
    MODEL_SERIALIZE_FILEPATH_PREFIX = "model"
    PREDICT_SERIALIZE_FILEPATH_PREFIX = "predict"

    def __init__(self, model: object, fit_params: dict):
        super().__init__()
        self.model = model
        self.fit_params = fit_params

    def get_model_name(self):
        return self.model.__class__.__name__

    def set_model_name(self, model_name):
        self.model.__class__.__name__ = model_name

    def get_params(self, deep=True):
        return deepcopy(self.fit_params) if deep \
            else self.fit_params

    def set_params(self, **params):
        for k, v in params.items():
            self.fit_params[k] = v

    def gen_model_serialize_filepath(self, suffix="pkl"):
        return self.add_models_prefix(
            self.get_model_name(),
            '.'.join([self.MODEL_SERIALIZE_FILEPATH_PREFIX,
                      concat_dict_key_values(self.fit_params),
                      suffix
                      ])
        )

    def gen_predict_serialize_filepath(self, suffix="tsv"):
        return self.add_models_prefix(
            self.get_model_name(),
            '.'.join([self.PREDICT_SERIALIZE_FILEPATH_PREFIX,
                      concat_dict_key_values(self.fit_params),
                      suffix
                      ])
        )


def safe_indexing(X, index):
    """From 'safe_indexing' in sklearn.utils.base"""
    if hasattr(X, "iloc"):
        # Work-around for indexing with read-only index in pandas
        index = index if index.flags.writeable else index.copy()
        # Pandas Dataframes and Series
        try:
            return X.iloc[index]
        except ValueError:
            return X.copy().iloc[index]
    elif hasattr(X, "shape"):
        if hasattr(X, 'take') \
                and (hasattr(index, 'dtype')
                     and index.dtype.kind == 'i'):
            # This is often substantially faster than X[index]
            return X.take(index, axis=0)
        else:
            return X[index]
    else:
        return [X[idx] for idx in index]


def safe_split(X, y, index):
    """From '_safe_split' in sklearn.utils.metaestimators"""
    X_subset = safe_indexing(X, index)
    y_subset = safe_indexing(y, index)

    return X_subset, y_subset


if __name__ == '__main__':
    print("Here is src/models/base.py")
