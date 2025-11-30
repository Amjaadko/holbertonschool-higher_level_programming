tuple_a = (1, 89)
tuple_b = (88, 11)

print(add_tuple(tuple_a, tuple_b))    # (89, 100)
print(add_tuple(tuple_a, (1, )))     # (2, 89)
print(add_tuple(tuple_a, ()))        # (1, 89)
