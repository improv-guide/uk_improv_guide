from typing import Sequence, Tuple


def opengraph_headers(title:str, image:str, url:str, type:str)->Sequence[Tuple[str,str]]:
    yield from [
        ("title",title),
        ("image",image),
        ("url", url),
        ("type",type)
    ]