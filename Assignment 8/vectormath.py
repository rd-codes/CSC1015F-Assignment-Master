# A program to calculate vector sum, dot product and the magnitude(Norm) of a vector
# 24 May 2021

from math import sqrt

# Return the sum of two vectors
def vector_sum(vector_a, vector_b):
    sum_of_vectors = []
    for index in range(3):
        sum_of_vectors.append(vector_a[index] + vector_b[index])
    return sum_of_vectors


# Return the dot product of two vectors
def dot_product(vector_a, vector_b):
    # Split each vector into its components
    x_comp_a = vector_a[0]
    y_comp_a = vector_a[1]
    z_comp_a = vector_a[2]
    
    x_comp_b = vector_b[0]
    y_comp_b = vector_b[1]
    z_comp_b = vector_b[2]
    
    product = x_comp_a * x_comp_b + y_comp_a * y_comp_b + z_comp_a * z_comp_b
    return round(product, 2)

# Return the magnitude(Norm) of a vector
def norm(vector):
    # Split a vector into its components
    x_comp_v = vector[0]
    y_comp_v = vector[1]
    z_comp_v = vector[2]
    norm_v = sqrt(x_comp_v ** 2 + y_comp_v ** 2 + z_comp_v ** 2)
    return "{0:.2f}".format(norm_v)


def main():
    vector_a = []
    vector_b = []
    a = input("Enter vector A:\n").split()
    b = input("Enter vector B:\n").split()
    # Store each component of the vectors in a number list
    for char_a in a:
        vector_a.append(eval(char_a))
    for char_b in b:
        vector_b.append(eval(char_b))
    print("A+B =", vector_sum(vector_a, vector_b))
    print("A.B =", dot_product(vector_a, vector_b))
    print("|A| =", norm(vector_a))
    print("|B| =", norm(vector_b))



if __name__ == "__main__":
    main()
