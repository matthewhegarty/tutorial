from unittest import IsolatedAsyncioTestCase, TestCase

#  Needs to be two test classes to see the issue


class OkTest(TestCase):
    def test_ok(self):
        self.assertEqual(1, 1)


class AsyncImportersTestCase(IsolatedAsyncioTestCase):
    async def test_copy_rows(self):
        self.assertEqual(1, 1)

