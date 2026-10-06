import unittest
from main import nearest_neighbor_two_opt, points_all, L1


class RouteTests(unittest.TestCase):
    def test_seed_and_route_cost(self):
        for count in (1, 2, 8, 12, 20):
            with self.subTest(count=count):
                result = nearest_neighbor_two_opt(range(count), 4, seed=42)
                self.assertEqual(result, nearest_neighbor_two_opt(range(count), 4, seed=42))
                cost, path = result
                self.assertEqual(sorted(path), list(range(count)))
                expected = sum(L1(points_all[a], points_all[b]) for a, b in zip(path, path[1:]))
                self.assertAlmostEqual(cost, expected)

    def test_empty_route(self):
        self.assertEqual(nearest_neighbor_two_opt([], seed=1), (0, []))

    def test_invalid_input(self):
        for indices, iterations in [([0, 0], 1), ([-1], 1), ([20], 1), ([0], 0)]:
            with self.subTest(indices=indices, iterations=iterations):
                with self.assertRaises(ValueError):
                    nearest_neighbor_two_opt(indices, iterations)


if __name__ == '__main__':
    unittest.main()
