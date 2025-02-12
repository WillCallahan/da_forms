class Da2404LineItem:
    def __init__(self, **kwargs):
        self.item_number = kwargs.get('item_number', '')
        self.status = kwargs.get('status', '')
        self.deficiencies = kwargs.get('deficiencies', '')
        self.corrective_action = kwargs.get('corrective_action', '')


class Da2404:
    def __init__(self, **kwargs):
        self.organization = kwargs.get('organization', '')
        self.nomenclature = kwargs.get('nomenclature', '')
        self.nsn = kwargs.get('nsn', '')
        self.miles = kwargs.get('miles', '')
        self.hours = kwargs.get('hours', '')
        self.rounds_fired = kwargs.get('rounds_fired', '')
        self.hot_starts = kwargs.get('hot_starts', '')
        self.date = kwargs.get('date', '')
        self.type_inspection = kwargs.get('type_inspection', '')
        self.tm_number_a = kwargs.get('tm_number_a', '')
        self.tm_date_a = kwargs.get('tm_date_a', '')
        self.tm_number_b = kwargs.get('tm_number_b', '')
        self.tm_date_b = kwargs.get('tm_date_b', '')
        self.time_a = kwargs.get('time_a', '')
        self.time_b = kwargs.get('time_b', '')
        self.man_hours_required = kwargs.get('man_hours_required', '')
        self.line_items = list(map(lambda v: Da2404LineItem(**v), kwargs.get('line_items', [])))
