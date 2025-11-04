class Model:
    mcmc = "foo"

model = Model()

print(dir(model))
print(hasattr(model, "__new__"))
