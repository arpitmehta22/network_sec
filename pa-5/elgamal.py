import random

q_1 = 717 #q
alpha_1 = 2 # alpha



class elgamal_code:
    def __init__(self, X1, q = q_1, alpha = alpha_1):
        """
        contructor 
        q prime number
        alpha alpha < q and alpha a primitive root of q
        Select private X1 X1 < q - 1
        Calculate  Ya = alpha X1 mod q
        Private key X1
        Public key PU = {q, alpha , Ya }
        """
        self.q = q
        self.alp = alpha
        self.X1 = X1
        self.Ya = pow(self.alp, self.X1, self.q)

    def Decrypter(self, r1, r2):
        """
        enceypted text: (r1 , r2 )
        Calc K = (r1 ) X1 mod q
        Plaintext: M = (r2 * K^-1) mod q
        """
        K = pow(r1, self.X1, self.q)
        M = (r2 * pow(K, -1, self.q)) % self.q
        
        return M
    def Encrypter(self, M):
        """
        Plaintext: M < q
        Select random integer k < q and put r1 = alpha^k mod q and K = (Ya)^k mod q
        r2 = KM mod q
        enceypted text: (r1 , r2 )
        """
        k  = random.randint(2, self.q - 1)
        K = pow(self.Ya, k, self.q)
        r1 = pow(self.alp, k, self.q)

        # calculating r2
        r2 = (K*M) % self.q

        return (r1, r2)