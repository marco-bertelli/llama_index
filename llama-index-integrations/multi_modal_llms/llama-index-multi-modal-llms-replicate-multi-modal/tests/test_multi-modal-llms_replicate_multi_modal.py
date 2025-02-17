from llama_index.core.multi_modal_llms.base import MultiModalLLM
from llama_index.multi_modal_llms.replicate_multi_modal import ReplicateMultiModal


def test_embedding_class():
    names_of_base_classes = [b.__name__ for b in ReplicateMultiModal.__mro__]
    assert MultiModalLLM.__name__ in names_of_base_classes
