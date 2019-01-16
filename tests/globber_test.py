# Copyright 2019 Jaakko Kangasharju
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import unittest

from globber import match


class GlobberTest(unittest.TestCase):

    def test_plain_pattern_matches_equal_file(self):
        self.assertTrue(match('dir/file.txt', os.path.join('dir', 'file.txt')))

    def test_plain_pattern_does_not_match_unequal_file(self):
        self.assertFalse(match('dir/file.txt', os.path.join('dir', 'file.csv')))

    def test_plain_pattern_requires_full_match(self):
        self.assertFalse(match('file.txt', os.path.join('dir', 'file.txt')))

    def test_trailing_slash_ignored_in_pattern(self):
        self.assertTrue(match('dir/file/', os.path.join('dir', 'file')))

    def test_trailing_slash_ignored_in_file_name(self):
        self.assertTrue(match('dir/file', os.path.join('dir', 'file', '')))

    def test_leading_slash_in_pattern_required_to_match(self):
        self.assertFalse(match('/dir/file.txt', os.path.join('dir', 'file.txt')))

    def test_leading_slash_in_file_name_required_to_match(self):
        self.assertFalse(match('dir/file.txt', os.path.join(os.sep, 'dir', 'file.txt')))

    def test_question_matches_one_character(self):
        self.assertTrue(match('dir/fil?.txt', os.path.join('dir', 'file.txt')))

    def test_question_does_not_match_multiple_characters(self):
        self.assertFalse(match('dir/fi?.txt', os.path.join('dir', 'file.txt')))

    def test_question_does_not_match_path_separator(self):
        self.assertFalse(match('dir?file.txt', os.path.join('dir', 'file.txt')))

    def test_star_matches_any_characters(self):
        self.assertTrue(match('dir/*.txt', os.path.join('dir', 'file.txt')))

    def test_star_matches_zero_characters(self):
        self.assertTrue(match('dir/file*.txt', os.path.join('dir', 'file.txt')))

    def test_star_does_not_match_path_separator(self):
        self.assertFalse(match('di*ile.txt', os.path.join('dir', 'file.txt')))

    def test_doublestar_matches_multiple_directories(self):
        self.assertTrue(match('dir/**/file.txt', os.path.join('dir', 'dir1', 'dir2', 'file.txt')))

    def test_doublestar_matches_zero_directories(self):
        self.assertTrue(match('dir/**/file.txt', os.path.join('dir', 'file.txt')))

    def test_doublestar_matches_in_the_beginning(self):
        self.assertTrue(match('**/file.txt', os.path.join('dir', 'dir1', 'file.txt')))

    def test_doublestar_matches_in_the_end(self):
        self.assertTrue(match('dir/**', os.path.join('dir', 'dir1', 'file.txt')))

    def test_only_doublestar_in_pattern_matches(self):
        self.assertTrue(match('**', os.path.join('dir', 'dir1', 'file.txt')))

    def test_doublestar_not_allowed_with_other_content(self):
        with self.assertRaises(ValueError):
            match('dir/**1/file.txt', os.path.join('dir', 'dir1', 'dir2', 'file.txt'))

    def test_repeated_doublestars_match(self):
        self.assertTrue(match('dir/**/**/file.txt', os.path.join('dir', 'file.txt')))

    def test_star_question_multiple_doublestar_matches(self):
        self.assertTrue(
            match('d*/**/dir3/**/fil?.txt', os.path.join('dir', 'dir1', 'dir2', 'dir3', 'dir4', 'dir5', 'file.txt')))

    def test_regex_special_characters_in_pattern_match_literally(self):
        self.assertTrue(match('dir/[f]ile.txt', os.path.join('dir', '[f]ile.txt')))

    def test_regex_wildcard_only_matches_literally(self):
        self.assertFalse(match('dir/file.txt', os.path.join('dir', 'file_txt')))

    def test_backslash_makes_question_non_special(self):
        self.assertTrue(match('dir/f\\?le.txt', os.path.join('dir', 'f?le.txt')))

    def test_backslash_makes_star_non_special(self):
        self.assertTrue(match('dir/\\**le.txt', os.path.join('dir', '*file.txt')))
