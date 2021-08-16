from django_fsm import transition as base_transition


def transition(
    field,
    source="*",
    target=None,
    on_error=None,
    conditions=[],
    permission=None,
    custom={},
):
    return base_transition(
        field,
        source="*",
        target=None,
        on_error=None,
        conditions=[],
        permission=None,
        custom={},
    )
