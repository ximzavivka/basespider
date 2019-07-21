class StatusMixin:
    STATUS = dict(
        EMPTY="Controller didn't start",
    )

    def is_empty(self):
        return self.status == "EMPTY"
