class BrowserHistory:
    # when vists remove all forward
    # when backward pop from backward and append to forward return top back
    # when forward pop from forward and append to backward reutrn top back

    def __init__(self, homepage: str):
        self.backwardStack = [homepage]
        self.forwardStack = []

    def visit(self, url: str) -> None:
        self.backwardStack.append(url)
        self.forwardStack = []

    def back(self, steps: int) -> str:
        while len(self.backwardStack) > 1 and steps:
            self.forwardStack.append(self.backwardStack.pop())
            steps -= 1

        return self.backwardStack[-1]      

    def forward(self, steps: int) -> str:
        while self.forwardStack and steps:
            self.backwardStack.append(self.forwardStack.pop())
            steps -= 1

        return self.backwardStack[-1]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)