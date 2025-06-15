# (P ∧ Q)
# If P AND Q are BOTH TRUE, then return True. Else Return False.
assert (True and True)   == True
assert (True and False)  == False
assert (False and True)  == False
assert (False and False) == False


# (P ∨ Q)
# If P OR Q OR BOTH are TRUE, then return True. Else Return False.
assert (True or True)   == True
assert (True or False)  == True
assert (False or True)  == True
assert (False or False) == False


# ¬P
# If P is True, return False. Else return True.
assert not True == False
assert not False == True
