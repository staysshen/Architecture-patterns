import unittest
from event_bus import EventBus
from component_a import ComponentA
from component_b import ComponentB

class EventBusTest(unittest.TestCase):
    def test_event_handling(self):
        # Arrange
        event_bus = EventBus()
        component_a = ComponentA()
        component_b = ComponentB()

        event_bus.subscribe("event_type_a", component_a.handle_event)
        event_bus.subscribe("event_type_b", component_b.handle_event)

        # Act
        event_bus.publish("event_type_a", "Event data for type A")
        event_bus.publish("event_type_b", "Event data for type B")
       
if __name__ == '__main__':
    unittest.main()
