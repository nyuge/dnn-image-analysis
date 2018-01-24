# Built-in modules
from os import pardir, path, makedirs

PROJECT_ROOT_DIRPATH = path.join(path.dirname(__file__), pardir, pardir)


def concat_dict_key_values(input_dict):
    output_string = str()
    for k, v in sorted(input_dict.items()):
        if isinstance(v, dict):
            for k_inner, v_inner in sorted(v.items()):
                if isinstance(v_inner, float):
                    output_string += "{ko}_{ki}_{v:.4f}.".format(ko=k, ki=k_inner, v=v_inner)
                else:
                    output_string += "{ko}_{ki}_{v}.".format(ko=k, ki=k_inner, v=v_inner)
        elif isinstance(v, float):
            output_string += "{k}_{v:.4f}.".format(k=k, v=v)
        else:
            output_string += "{k}_{v}.".format(k=k, v=v)

    return output_string[:-1]


class PathHandlerBase(object):
    def __init__(self):
        self.PROJECT_ROOT_DIRPATH = PROJECT_ROOT_DIRPATH
        self.RAW_DATA_DIRPATH = path.join(PROJECT_ROOT_DIRPATH, "data", "raw")
        self.INTERIM_DATA_DIRPATH = path.join(PROJECT_ROOT_DIRPATH, "data", "interim")
        self.PROCESSED_DATA_DIRPATH = path.join(PROJECT_ROOT_DIRPATH, "data", "processed")
        self.MODELS_DIRPATH = path.join(PROJECT_ROOT_DIRPATH, "models")
        self.REPORTS_FIGURES_DIRPATH = path.join(PROJECT_ROOT_DIRPATH, "reports", "figures")

    @staticmethod
    def gen_abspath(relpath):
        abspath = path.abspath(relpath)
        makedirs(path.dirname(abspath), exist_ok=True)

        return abspath

    def add_raw_data_prefix(self, *args):
        return self.gen_abspath(path.join(self.RAW_DATA_DIRPATH, *args))

    def add_interim_data_prefix(self, *args):
        return self.gen_abspath(path.join(self.INTERIM_DATA_DIRPATH, *args))

    def add_processed_data_prefix(self, *args):
        return self.gen_abspath(path.join(self.PROCESSED_DATA_DIRPATH, *args))

    def add_models_prefix(self, *args):
        return self.gen_abspath(path.join(self.MODELS_DIRPATH, *args))

    def add_reports_figures_prefix(self, *args):
        return self.gen_abspath(path.join(self.REPORTS_FIGURES_DIRPATH, *args))


if __name__ == "__main__":
    print("Here is src/utils/base.py")
