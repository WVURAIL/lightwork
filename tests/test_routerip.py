import os
from pathlib import Path
import subprocess
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / "bin" / "routerip"

class RouterLookupTests(unittest.TestCase):
    def lookup(self, route):
        environment = dict(os.environ, ROUTE_FIXTURE=route)
        command = 'netstat() { printf "%s\\n" "$ROUTE_FIXTURE"; }; source "$1"'
        return subprocess.run(["bash", "-c", command, "bash", str(SCRIPT)], env=environment, capture_output=True, text=True, check=True).stdout.strip()

    def test_linux_default_route(self):
        self.assertEqual(self.lookup("0.0.0.0 192.168.10.1 0.0.0.0 UG 0 0 0 eth0"), "192.168.10.1")

    def test_bsd_default_route(self):
        self.assertEqual(self.lookup("default 192.168.10.1 UGSc en0"), "192.168.10.1")

    def test_missing_default_route(self):
        self.assertEqual(self.lookup("192.168.10.0 0.0.0.0 U en0"), "")

if __name__ == "__main__":
    unittest.main()
