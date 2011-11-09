import py
from js.jsobj import W_IntNumber, W_FloatNumber, w_Null, w_Undefined, w_True, w_False, NAN, W_String, W__Object as W_Object, W_BasicObject, W_BooleanObject

def test_intnumber():
    n = W_IntNumber(0x80000000)
    assert n.ToInt32() == -0x80000000
    assert n.ToUInt32() == 0x80000000

def test_floatnumber():
    n = W_FloatNumber(0x80000000)
    assert n.ToInt32() == -0x80000000
    assert n.ToUInt32() == 0x80000000

class TestType():
    def test_undefined(self):
        assert w_Undefined.type() == 'undefined'

    def test_null(self):
        assert w_Null.type() == 'null'

    def test_boolean(self):
        assert w_True.type() == 'boolean'
        assert w_False.type() == 'boolean'

    def test_number(self):
        assert W_IntNumber(0).type() == 'number'
        assert W_FloatNumber(0.0).type() == 'number'
        assert W_FloatNumber(NAN).type() == 'number'

    def test_string(self):
        assert W_String('').type() == 'string'

    def test_object(self):
        assert W_Object().type() == 'object'

class TestToBoolean():
    def test_undefined(self):
        assert w_Undefined.ToBoolean() == False

    def test_null(self):
        assert w_Null.ToBoolean() == False

    def test_boolean(self):
        assert w_True.ToBoolean() == True
        assert w_False.ToBoolean() == False

    def test_number(self):
        assert W_IntNumber(0).ToBoolean() == False
        assert W_IntNumber(1).ToBoolean() == True
        assert W_FloatNumber(0.0).ToBoolean() == False
        assert W_FloatNumber(1.0).ToBoolean() == True
        assert W_FloatNumber(NAN).ToBoolean() == False

    def test_string(self):
        assert W_String('').ToBoolean() == False
        assert W_String('a').ToBoolean() == True

    def test_object(self):
        assert W_Object().ToBoolean() == True

class TestToNumber():
    def test_undefined(self):
        assert w_Undefined.ToNumber() is NAN

    def test_null(self):
        assert w_Null.ToNumber() == 0

    def test_boolean(self):
        assert w_True.ToNumber() == 1
        assert w_False.ToNumber() == 0

    def test_number(self):
        assert W_IntNumber(0).ToNumber() == 0
        assert W_IntNumber(1).ToNumber() == 1
        assert W_FloatNumber(0.0).ToNumber() == 0
        assert W_FloatNumber(1.0).ToNumber() == 1.0
        assert W_FloatNumber(NAN).ToNumber() is NAN

    def test_string(self):
        assert W_String('').ToNumber() == 0
        assert W_String('x').ToNumber() is NAN
        assert W_String('1').ToNumber() == 1

    def test_object(self):
        py.test.skip()
        W_Object().ToNumber()

class TestToString():
    def test_undefined(self):
        assert w_Undefined.ToString() == 'undefined'

    def test_null(self):
        assert w_Null.ToString() == 'null'

    def test_boolean(self):
        assert w_True.ToString() == 'true'
        assert w_False.ToString() == 'false'

    def test_number(self):
        assert W_IntNumber(0).ToString() == '0'
        assert W_IntNumber(1).ToString() == '1'
        assert W_FloatNumber(0.0).ToString() == '0'
        assert W_FloatNumber(1.0).ToString() == '1'
        assert W_FloatNumber(NAN).ToString() == 'NaN'

    def test_string(self):
        assert W_String('').ToString() == ''
        assert W_String('x').ToString() == 'x'
        assert W_String('1').ToString() == '1'

    def test_object(self):
        py.test.skip()
        W_Object().ToString()

class TestW_BasicObject():
    def test_Prototype(self):
        assert W_BasicObject().Prototype() is None

    def test_Class(self):
        assert W_BasicObject().Class() == 'Object'

class Test_WBooleanObject():
    def test_toPrimitive(self):
        py.test.skip()
        b = W_BooleanObject(w_True)
        assert b.ToPrimitive() == w_True
