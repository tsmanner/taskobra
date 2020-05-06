from datetime import datetime
from ..ORMTestCase import ORMTestCase
from taskobra.orm import get_engine, get_session, Snapshot, System


class TestSystemSnapshot(ORMTestCase):
    def test_SystemSnapshot_creation(self):
        with self.subTest("Snapshot added to System"):
            system = System()
            snapshot = Snapshot(timestamp=datetime(2020, 3, 9, 9, 53, 53))
            system.snapshots.append(snapshot)

            [self.assertIs(system, snapshot.system) for snapshot in system.snapshots]
            self.assertIs(snapshot, system.snapshots[0])
        with self.subTest("System added to Snapshot"):
            system = System()
            snapshot = Snapshot(timestamp=datetime(2020, 3, 9, 9, 53, 53))
            snapshot.system = system

            [self.assertIs(system, snapshot.system) for snapshot in system.snapshots]
            self.assertIs(snapshot, system.snapshots[0])
