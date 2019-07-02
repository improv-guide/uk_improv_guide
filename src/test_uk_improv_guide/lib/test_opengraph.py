from src.uk_improv_guide.uk_improv_guide.lib.opengraph import opengraph_website


def test_opengraph0():

    result = opengraph_website(
        title="title", image="http://foo", type="xxx", url="http://bar"
    )
