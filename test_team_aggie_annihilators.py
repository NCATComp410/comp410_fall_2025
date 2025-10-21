def test_au_medicare(self):
    """Test AU_MEDICARE with proper format + modulus-10 checksum (first 8 digits; 9th is check digit)."""
    import re

    # Regex: XXXX XXXXX X  (10 digits with spaces: 4 + 5 + 1)
    medicare_pattern = re.compile(r"\b\d{4}\s\d{5}\s\d\b")

    # Local helper: checksum for first 8 digits per AU Medicare spec
    def checksum_first8(d8: str) -> int:
        weights = [1, 3, 7, 9, 1, 3, 7, 9]
        return sum(int(d) * w for d, w in zip(d8, weights)) % 10

    # --- TA examples (must behave differently due to checksum) ---
    valid_example = "2123 45670 1"    # 9th digit (0) matches sum(first8)%10
    invalid_example = "2123 25870 1"  # wrong checksum at 9th digit

    # Format checks (regex should match both; checksum distinguishes them)
    self.assertRegex(valid_example, medicare_pattern, "Regex failed on valid formatted example")
    self.assertRegex(invalid_example, medicare_pattern, "Regex should match format even when checksum is wrong")

    # Checksum math sanity
    v_digits = valid_example.replace(" ", "")
    i_digits = invalid_example.replace(" ", "")
    self.assertEqual(checksum_first8(v_digits[:8]), int(v_digits[8]), "Valid example checksum should match 9th digit")
    self.assertNotEqual(checksum_first8(i_digits[:8]), int(i_digits[8]), "Invalid example checksum should NOT match 9th digit")

    # Analyzer behavior: detect valid, ignore invalid
    self.assertGreater(len(analyze_text(valid_example, ['AU_MEDICARE'])), 0, "Expected AU_MEDICARE detection for valid example")
    self.assertListEqual(analyze_text(invalid_example, ['AU_MEDICARE']), [], "Should not detect AU_MEDICARE for invalid checksum")

    # --- Programmatic cases: build valid & invalid numbers using checksum ---
    # Each item is an 8-digit base (first 4 + next 4); 9th digit is computed; 10th digit (IRN) can be 0-9 and is not part of checksum
    base8_list = ["12345678", "23451111", "98766543", "21234567", "34561234"]
    irns = ["0", "1", "2", "9"]

    for base8 in base8_list:
        p4 = base8[:4]
        n4 = base8[4:]  # positions 5–8
        cd = checksum_first8(base8)  # 9th digit
        for irn in irns:
            # Valid number
            valid_num = f"{p4} {n4}{cd} {irn}"
            self.assertRegex(valid_num, medicare_pattern, f"Regex failed on: {valid_num}")
            self.assertGreater(len(analyze_text(valid_num, ['AU_MEDICARE'])), 0, f"Expected detection for valid: {valid_num}")

            # Invalid number: flip checksum digit but keep format
            bad_cd = (cd + 1) % 10
            invalid_num = f"{p4} {n4}{bad_cd} {irn}"
            self.assertRegex(invalid_num, medicare_pattern, f"Regex failed on: {invalid_num}")
            self.assertListEqual(analyze_text(invalid_num, ['AU_MEDICARE']), [], f"Should not detect invalid checksum: {invalid_num}")

    # Negative: no number present
    none_text = "my medicare number is hidden"
    self.assertNotRegex(none_text, medicare_pattern)
    self.assertListEqual(analyze_text(none_text, ['AU_MEDICARE']), [])
