from lxml import etree
from functools import lru_cache
from numba import njit


class LxmlSoup:
    def __init__(self, html_content):
        self.root = etree.HTML(html_content)

    @lru_cache(maxsize=128)  # Set an appropriate maxsize for your use case
    @njit(parallel=True)
    def findel(self, tag=None, **attrs):
        xpath = self._build_xpath(tag, **attrs)
        elements = self.root.xpath(xpath)
        return [LxmlElement(element) for element in elements]

    @lru_cache(maxsize=128)
    def find_all(self, tag=None, **attrs):
        xpath = self._build_xpath(tag, **attrs)
        elements = self.root.xpath(xpath)
        return [LxmlElement(element) for element in elements]

    @lru_cache(maxsize=128)
    def find(self, tag=None, **attrs):
        elements = self.findel(tag, **attrs)
        if elements:
            return elements[0]
        return None

    def select(self, selector):
        elements = self.root.cssselect(selector)
        return [LxmlElement(element) for element in elements]

    def select_one(self, selector):
        elements = self.root.cssselect(selector)
        if elements:
            return LxmlElement(elements[0])
        return None

    def _build_xpath(self, tag=None, **attrs):
        xpath = "//"
        if tag:
            xpath += tag
        if attrs:
            predicates = []
            for key, value in attrs.items():
                if key == 'class_':
                    key = key[0:-1]
                predicates.append(f'[@{key}="{value}"]')
            xpath += "".join(predicates)
        return xpath

    def text(self):
        return ''.join(self.root.xpath(".//text()")).strip()


class LxmlElement:
    def __init__(self, element):
        self.element = element

    @njit(parallel=True)
    def findel(self, tag=None, **attrs):
        xpath = self._build_xpath(tag, **attrs)
        elements = self.element.xpath(xpath)
        return [LxmlElement(element) for element in elements]

    def find_all(self, tag=None, **attrs):
        xpath = self._build_xpath(tag, **attrs)
        elements = self.element.xpath(xpath)
        return [LxmlElement(element) for element in elements]

    def find(self, tag=None, **attrs):
        elements = self.findel(tag, **attrs)
        if elements:
            return elements[0]
        return None

    def select(self, selector):
        elements = self.element.cssselect(selector)
        return [LxmlElement(element) for element in elements]

    def select_one(self, selector):
        elements = self.element.cssselect(selector)
        if elements:
            return LxmlElement(elements[0])
        return None

    def _build_xpath(self, tag=None, **attrs):
        xpath = ".//"
        if tag:
            xpath += tag
        if attrs:
            predicates = []
            for key, value in attrs.items():
                if key == 'class_':
                    key = key[0:-1]
                predicates.append(f'[@{key}="{value}"]')
            xpath += "".join(predicates)
        return xpath

    def text(self):
        return ''.join(self.element.xpath(".//text()")).strip()

    def attribute(self, name):
        return self.element.get(name)

    def get(self, name, default=None):
        return self.element.get(name, default)

    def to_html(self):
        return etree.tostring(self.element, encoding='unicode')

    def __str__(self):
        return etree.tostring(self.element, encoding='unicode')

    def __repr__(self):
        return str(self)

    def __call__(self):
        return self.element.text_content()

    def has_attr(self, name):
        return name in self.element.attrib

    def has_class(self, class_name):
        class_attr = self.element.get('class')
        if class_attr:
            classes = class_attr.split()
            return class_name in classes
        return False

    def parent(self):
        parent_element = self.element.getparent()
        if parent_element is not None:
            return LxmlElement(parent_element)
        return None

    def next_sibling(self):
        next_sibling_element = self.element.getnext()
        if next_sibling_element is not None:
            return LxmlElement(next_sibling_element)
        return None

    def previous_sibling(self):
        previous_sibling_element = self.element.getprevious()
        if previous_sibling_element is not None:
            return LxmlElement(previous_sibling_element)
        return None

    def children(self):
        elements = self.element.xpath(".")
        return [LxmlElement(element) for element in elements]

    def next_siblings(self):
        elements = self.element.xpath("following::*")
        return [LxmlElement(element) for element in elements]

    def previous_siblings(self):
        elements = self.element.xpath("preceding::*")
        return [LxmlElement(element) for element in elements]





