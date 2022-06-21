import unittest

from util.util import replace_params

class TestReplaceParams(unittest.TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def test_replace(self):
        default = {"eat_pizza": True,   "with_pineapple": False}

        result = replace_params(default, **{})
        self.assertEqual(result['eat_pizza'],       True)
        self.assertEqual(result['with_pineapple'],  False)

        result = replace_params(default, **{"eat_pizza": False})
        self.assertEqual(result['eat_pizza'],       False)
        self.assertEqual(result['with_pineapple'],  False)

        result = replace_params(default, **{"with_pineapple": True})
        self.assertEqual(result['eat_pizza'],       True)
        self.assertEqual(result['with_pineapple'],  True)

        result = replace_params(default, **{"eat_pizza": False, "with_pineapple": True})
        self.assertEqual(result['eat_pizza'],       False)
        self.assertEqual(result['with_pineapple'],  True)

    def test_replace_with_not_existing_key(self):
        default = { "eat_pizza": True }

        result = replace_params(default, **{})
        self.assertTrue('eat_pizza' in result)
        
        result = replace_params(default, **{"with_pineapple": True})
        self.assertTrue('eat_pizza' in result)
        self.assertFalse('with_pineapple' in result) # Since replacing, new params should not be in the result.
