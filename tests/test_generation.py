import unittest

from ventura_genart import ArtConfig, fingerprint, generate_svg


class GenerationTests(unittest.TestCase):
    def test_same_seed_is_reproducible(self):
        config = ArtConfig(seed="release-1", circles=6)
        first = generate_svg(config)
        second = generate_svg(config)
        self.assertEqual(first, second)
        self.assertEqual(fingerprint(first), fingerprint(second))
        self.assertEqual(first.count("<circle "), 6)

    def test_different_seed_changes_output(self):
        self.assertNotEqual(
            fingerprint(generate_svg(ArtConfig(seed="a"))),
            fingerprint(generate_svg(ArtConfig(seed="b"))),
        )

    def test_invalid_config_fails(self):
        with self.assertRaises(ValueError):
            generate_svg(ArtConfig(width=0))
        with self.assertRaises(ValueError):
            generate_svg(ArtConfig(circles=0))


if __name__ == "__main__":
    unittest.main()
