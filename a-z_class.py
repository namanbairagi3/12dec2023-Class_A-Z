class A(): #Base class
    #1.1 Property=Variable
    myName = "naman"
    #1.2 Constructoris a special Function/Method
    #1.3 Method=Function

class B(A):
    pass

class C(B):
    pass

class D(C):
    pass

class E(D):
    pass

class F(E):
    pass

class G(F):
    pass

class H(G):
    pass

class I(H):
    pass

class J(I):
    pass

class K(J):
    pass

class L(K):
    pass

class M(L):
    pass

class N(M):
    pass

class P(N):
    pass

class Q(P):
    pass

class R(Q):
    pass

class S(R):
    pass

class T(S):
    pass

class U(T):
    pass

class V(U):
    pass

class W(V):
    pass

class X(W):
    pass

class Y(X):
    pass

class Z(Y):
    def getMyName(self):
        print(f"My Name is {self.myName}")

# Create class object
co = Z()
co.getMyName()
