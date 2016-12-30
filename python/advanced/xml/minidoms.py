# coding: utf-8
"""
['ATTRIBUTE_NODE', 'CDATA_SECTION_NODE', 'COMMENT_NODE', 'DOCUMENT_FRAGMENT_NODE', 'DOCUMENT_NODE', 'DOCUMENT_TYPE_NODE', 'ELEMENT_NODE', 'ENTI
TY_NODE', 'ENTITY_REFERENCE_NODE', 'NOTATION_NODE', 'PROCESSING_INSTRUCTION_NODE', 'TEXT_NODE', '__doc__', '__init__', '__module__', '__nonzero__', '__repr__', '_attrs', '_attrsNS', '_call_user_data_handler', '_child_node_types', '_get_attributes', '_get_childNodes', '_get_firstChild','_get_lastChild', '_get_localName', '_get_tagName', '_magic_id_nodes', 'appendChild', 'attributes', 'childNodes', 'cloneNode', 'firstChild', 'getAttribute', 'getAttributeNS', 'getAttributeNode', 'getAttributeNodeNS', 'getElementsByTagName', 'getElementsByTagNameNS', 'getInterface', 'getUserData', 'hasAttribute', 'hasAttributeNS', 'hasAttributes', 'hasChildNodes', 'insertBefore', 'isSameNode', 'isSupported', 'lastChild', 'localName', 'namespaceURI', 'nextSibling', 'nodeName', 'nodeType', 'nodeValue', 'normalize', 'ownerDocument', 'parentNode', 'prefix', 'previousSibling', 'removeAttribute', 'removeAttributeNS', 'removeAttributeNode', 'removeAttributeNodeNS', 'removeChild', 'replaceChild', 'schemaType', 'setAttribute', 'setAttributeNS', 'setAttributeNode', 'setAttributeNodeNS', 'setIdAttribute', 'setIdAttributeNS', 'setIdAttributeNode', 'setUserData', 'tagName', 'toprettyxml', 'toxml', 'unlink', 'writexml']
"""
__author__ = u'lovexiaov'

import os
from xml.dom import minidom

xml_document = minidom.parse(os.path.split(__file__)[0] + r'/tmp.xml') # Get document obj
root = xml_document.documentElement # Get root element

treechilds = root.getElementsByTagName(u'TreeChildItem') # Get all tags by given name

target_node = treechilds[-1].parentNode

# for child in target_node.childNodes:
#     if(isinstance(child, minidom.Element)):
#         print(child.tagName)

print(len(target_node.parentNode.childNodes))
for child in target_node.parentNode.childNodes:
    if isinstance(child, minidom.Element):
        print(child.tagName)


if __name__ == u'__main__':
    pass