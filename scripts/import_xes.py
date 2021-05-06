import sys
from pm4py import get_attributes, get_start_activities, get_end_activities, get_attribute_values, get_variants_as_tuples
from pm4py.objects.log.importer.xes import importer as xes_importer


def import_xes(file_path):
    event_log = xes_importer.apply(file_path)
    num_events = len(event_log)
    event_attributes = get_attributes(event_log)
    attribute_values = get_attribute_values(event_log, "concept:name")
    start_activities = get_start_activities(event_log)
    end_activities = get_end_activities(event_log)
    num_variants = len(get_variants_as_tuples(event_log))
    print("Number of events: {}\nEvent level attributes: {}\nAttribute values and their counter: {}\nNumber of start activities: {}\nStart activities: {}\nNumber of end activities: {}\nEnd activities: {}\nNumber of variants: {}".format(
        num_events, event_attributes, attribute_values, len(start_activities), start_activities, len(end_activities), end_activities, num_variants))
    return event_log


if __name__ == "__main__":
    import_xes(sys.argv[1])
