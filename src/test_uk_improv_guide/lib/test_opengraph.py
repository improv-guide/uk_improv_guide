from src.uk_improv_guide.uk_improv_guide.lib.opengraph import opengraph_headers


def test_opengraph0():

    result = opengraph_headers(
        title="title",
        image="http://foo",
        type="xxx",
        url="http://bar"
    )

