class Solution:
    def isPrefix(self, c, product):
        if len(c) > len(product):
            return False
        for i in range(len(c)):
            if c[i] != product[i]:
                return False
        return True

    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        res = []

        for i in range(len(searchWord)):
            c = searchWord[:i+1]
            cur = []
            for product in products:
                if self.isPrefix(c, product):
                    cur.append(product)
            res.append(cur[:3])

        return res