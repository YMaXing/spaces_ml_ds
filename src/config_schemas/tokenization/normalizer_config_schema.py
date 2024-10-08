from dataclasses import dataclass, field
from typing import Any, Optional

from hydra.core.config_store import ConfigStore
from omegaconf import MISSING, SI


@dataclass
class NormalizerConfig:
    _target_: str = MISSING


@dataclass
class BertNormalizerConfig(NormalizerConfig):
    _target_: str = "tokenizers.normalizers.BertNormalizer"
    clean_text: bool = True
    handle_chinese_chars: bool = True
    strip_accents: bool = True
    lowercase: bool = True


@dataclass
class LowercaseNormalizerConfig(NormalizerConfig):
    _target_: str = "tokenizers.normalizers.Lowercase"


@dataclass
class NFKDNormalizerConfig(NormalizerConfig):
    _target_: str = "tokenizers.normalizers.NFKD"


@dataclass
class NFCNormalizerConfig(NormalizerConfig):
    _target_: str = "tokenizers.normalizers.NFC"


@dataclass
class NFDNormalizerConfig(NormalizerConfig):
    _target_: str = "tokenizers.normalizers.NFD"


@dataclass
class NFKCNormalizerConfig(NormalizerConfig):
    _target_: str = "tokenizers.normalizers.NFKC"


@dataclass
class NmtNormalizerConfig(NormalizerConfig):
    _target_: str = "tokenizers.normalizers.Nmt"


@dataclass
class ReplaceNormalizerConfig(NormalizerConfig):
    _target_: str = "tokenizers.normalizers.Replace"
    pattern: str = MISSING
    content: str = MISSING


@dataclass
class SequenceNormalizerConfig(NormalizerConfig):
    _target_: str = "tokenizers.normalizers.Sequence"
    normalizers: list[NormalizerConfig] = field(default_factory=lambda: [])
    _normalizers_dict: dict[str, NormalizerConfig] = field(default_factory=lambda: {})


@dataclass
class StripNormalizerConfig(NormalizerConfig):
    _target_: str = "tokenizers.normalizers.Strip"
    left: bool = True
    right: bool = True


@dataclass
class StripAccentsNormalizerConfig(NormalizerConfig):
    _target_: str = "tokenizers.normalizers.StripAccents"


def setup_config() -> None:
    cs = ConfigStore.instance()

    cs.store(name="normalizer_schema", node=NormalizerConfig)

    cs.store(name="bert_normalizer_schema", node=BertNormalizerConfig, group="tokenizer/nomalizer")

    cs.store(name="lowercase_normalizer_schema", node=LowercaseNormalizerConfig, group="tokenizer/nomalizer")

    cs.store(name="nfkd_normalizer_schema", node=NFKDNormalizerConfig, group="tokenizer/nomalizer")

    cs.store(name="nfc_normalizer_schema", node=NFCNormalizerConfig, group="tokenizer/nomalizer")

    cs.store(name="nfd_normalizer_schema", node=NFDNormalizerConfig, group="tokenizer/nomalizer")

    cs.store(name="nfkc_normalizer_schema", node=NFKCNormalizerConfig, group="tokenizer/nomalizer")

    cs.store(name="nmt_normalizer_schema", node=NmtNormalizerConfig, group="tokenizer/nomalizer")

    cs.store(name="replace_normalizer_schema", node=ReplaceNormalizerConfig, group="tokenizer/nomalizer")

    cs.store(name="sequence_normalizer_schema", node=SequenceNormalizerConfig, group="tokenizer/nomalizer")

    cs.store(name="strip_normalizer_schema", node=StripNormalizerConfig, group="tokenizer/nomalizer")

    cs.store(name="strip_accents_normalizer_schema", node=StripAccentsNormalizerConfig, group="tokenizer/nomalizer")
