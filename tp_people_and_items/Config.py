from mcdreforged.api.utils import Serializable


class Config(Serializable):
    enable_tpp: bool = True     # tp personally
    enable_tpbc: bool = True    # tp broadcast

    @classmethod
    def load(cls) -> 'Config':
        pass
