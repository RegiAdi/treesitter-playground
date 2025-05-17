import tree_sitter_python as tspy
from tree_sitter import Language, Parser

PYLANG = Language(tspy.language())
parser = Parser(PYLANG)

tree = parser.parse(
    bytes(
        """
def foo():
    if bar:
        baz()
    else:
        bar()
        """,
        "utf8"
    )
)

root_node = tree.root_node
print(root_node)

assert root_node.type == 'module'
print("Test passed! root_node.type: ", root_node.type)

assert root_node.start_point == (1, 0)
print("Test passed! root_node.start_point: ", root_node.start_point)
