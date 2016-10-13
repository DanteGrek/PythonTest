class SoftAssert:

    fails = []

    def assert_true(self, expression, message):
        try:
            assert expression
        except AssertionError:
            self.fails.append(message)
        finally:
            return self

    def assert_equals(self, actual, expected, message):
        try:
            expression = actual == expected
            assert_message = "{} Expected: '{}' but found: '{}'".format(message, expected, actual)
            assert expression, assert_message
        except AssertionError:
            self.fails.append(assert_message)
        finally:
            return self

    def assert_all(self):
        assert not self.fails, self.fails

if __name__ == '__main__':
    soft = SoftAssert()
    soft.assert_true(False, "my message")\
        .assert_true(False, "my message 2")\
        .assert_true(False, "my message 3")\
        .assert_equals(2, 3, "equals message")\
        .assert_all()
