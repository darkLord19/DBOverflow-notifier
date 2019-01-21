class Database:
    def __init__(
        self,
        table_name,
        field_name,
        field_datatype,
        field_minvlaue,
        field_maxvalue,
        current_max,
    ):
        self.table_name = table_name
        self.field_name = field_name
        self.field_datatype = field_datatype
        self.field_minvlaue = field_minvlaue
        self.field_maxvalue = field_maxvalue
        self.current_max = current_max
