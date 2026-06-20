"""
Fast Fourier Transform (FFT)
Implements the Cooley-Tukey Radix-2 algorithm for:
1. Forward Fast Fourier Transform (FFT)
2. Inverse Fast Fourier Transform (IFFT)
3. Polynomial Multiplication in O(N log N) time (instead of O(N^2) naive convolution).
Time Complexity: O(N log N)
Space Complexity: O(N) recursion stack.
"""

import cmath

def fft(a):
    """
    Computes the Discrete Fourier Transform (DFT) of a sequence.
    Input sequence length must be a power of 2.
    """
    n = len(a)
    if n <= 1:
        return a
        
    # Divide step: split into even and odd indices
    even = fft(a[0::2])
    odd = fft(a[1::2])
    
    # Combine step using twiddle factors
    # W_n^k = exp(-2j * pi * k / n)
    t = [cmath.exp(-2j * cmath.pi * k / n) * odd[k] for k in range(n // 2)]
    
    # Recombine results
    left = [even[k] + t[k] for k in range(n // 2)]
    right = [even[k] - t[k] for k in range(n // 2)]
    
    return left + right

def ifft(a):
    """
    Computes the Inverse Discrete Fourier Transform (IDFT) of a sequence.
    Input sequence length must be a power of 2.
    """
    n = len(a)
    # Conjugate the input
    a_conj = [x.conjugate() for x in a]
    # Apply forward FFT
    transformed = fft(a_conj)
    # Conjugate back and divide by N
    res = [x.conjugate() / n for x in transformed]
    return res

def multiply_polynomials(p1, p2):
    """
    Multiplies two polynomials p1 and p2 represented as lists of coefficients.
    Returns: list of coefficients of the product.
    e.g. p1 = [1, 2] represents 1 + 2x.
    """
    # Size of result polynomial will be len(p1) + len(p2) - 1
    target_size = len(p1) + len(p2) - 1
    
    # Pad to next power of 2
    n = 1
    while n < target_size:
        n *= 2
        
    # Pad coefficients with zeros
    p1_padded = p1 + [0] * (n - len(p1))
    p2_padded = p2 + [0] * (n - len(p2))
    
    # 1. Transform coefficients to point-value form (FFT)
    p1_dft = fft(p1_padded)
    p2_dft = fft(p2_padded)
    
    # 2. Pointwise multiplication
    product_dft = [p1_dft[i] * p2_dft[i] for i in range(n)]
    
    # 3. Interpolate back to coefficient form (IFFT)
    product_coeff = ifft(product_dft)
    
    # Extract real parts and round to nearest integer, trim to target_size
    return [round(x.real) for x in product_coeff[:target_size]]

if __name__ == "__main__":
    print("=== Fast Fourier Transform (FFT) Demo ===")
    
    # 1. Forward and Inverse FFT test
    signal = [1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0]
    print(f"Original Signal: {signal}")
    
    dft_val = fft(signal)
    print("\nFFT Output:")
    for x in dft_val:
        print(f"  {x.real:7.3f} + {x.imag:7.3f}j")
        
    reconstructed = ifft(dft_val)
    reconstructed_real = [round(x.real, 3) for x in reconstructed]
    print(f"\nReconstructed Signal (IFFT): {reconstructed_real}")
    
    # 2. Polynomial Multiplication test
    # p1 = 1 + 2x (coefficients: [1, 2])
    # p2 = 3 + 4x (coefficients: [3, 4])
    # Product: (1 + 2x)(3 + 4x) = 3 + 10x + 8x^2 (coefficients: [3, 10, 8])
    p1 = [1, 2]
    p2 = [3, 4]
    prod = multiply_polynomials(p1, p2)
    print(f"\nPolynomial Multiplication:")
    print(f"  ({p1}) * ({p2}) = {prod} (Expected: [3, 10, 8])")
