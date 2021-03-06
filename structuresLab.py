import numpy as np
import matplotlib.pyplot as plt

E = 69*10**3                #given in N/mm^2

a_array = [1.4563, 52.6604, 1.4563]
b_array = [23.5160, 1.4563, 23.103]

y_array = [-27.0584, 0.0, 27.0584]
z_array = [11.0299, 0.0, -10.8234]

m_array = [0.5, 1., 1.5, 2., 2.5, 3., 2.5, 2., 1.5, 1., 0.5]

ex1 = [13., 28., 39., 55., 66., 77., 68., 61., 53., 43., 34.]
ex2 = [21., 26., 42., 64., 88., 108., 90., 69., 46., 29., 21.]
ex3 = [-10., -19., -32., -44., -60., -70., -60., -43., -31., -19., -8.]
ex4 = [-18., -40., -63., -81., -112., -131., -113., -86., -66., -45., -21.]

l_array = [574., 573., 571.5, 571.]

gauge_y = [-27.7865, -12.4365, 27.7865, 12.7265]
gauge_z = [11.2719, -0.7282, -10.6619, 0.7282]

vb = [0.23, 0.52, 0.78, 1.05, 1.32, 1.6, 1.33, 1.06, 0.79, 0.53, 0.27]
wb = [0.36, 0.8, 1.2, 1.62, 2.04, 2.47, 2.07, 1.67, 1.25, 0.84, 0.45]

l_beam = 643.67


def subArea(a_array, b_array):
    area_array = []
    for i in range(len(a_array)):
        area_array.append(round(a_array[i]*b_array[i], 4))
    
    print("\n\t The total area is: " + str(sum(area_array)) + " mm^4")
    return area_array


def SMA(a_array, b_array, y_array, z_array):
    Ay_array = []
    Az_array = []
    global Iy
    Iy = []
    global Iz
    Iz = []
    global Iyz
    Iyz = []
    A_array = subArea(a_array, b_array)
    for i in range(len(A_array)):
        Ay_array.append(A_array[i]*y_array[i])
        Az_array.append(A_array[i]*z_array[i])
        Iy.append(A_array[i]*(z_array[i]**2)+((b_array[i]**3)*a_array[i])/12)
        Iz.append(A_array[i]*(y_array[i]**2)+((a_array[i]**3)*b_array[i])/12)
        Iyz.append(A_array[i]*z_array[i]*y_array[i])
    #round(sum(Ay_array), 4), round(sum(Az_array), 4)
    #round(sum(Iy), 4), round(sum(Iz), 4), round(sum(Iyz), 4)
    return round(np.rad2deg(np.arctan(round(sum(Iyz), 4)/round(sum(Iy), 4))), 3)


def plotStrainData(m_array, ex1, ex2, ex3, ex4):
    
    yerr4 = 0.00001
    pred_plot_x = np.arange(1, 30, 4)
    
    M = [9.81*x for x in m_array]
    
    ex1 = [x*10**(-6) for x in ex1]
    ex2 = [x*10**(-6) for x in ex2]
    ex3 = [x*10**(-6) for x in ex3]
    ex4 = [x*10**(-6) for x in ex4]
    
    col1 = []
    col2 = []
    col3 = []
    col4 = []
    
    for i in range(len(M)):
        col1.append(round(ex1[i]/M[i], 3))
        col2.append(round(ex2[i]/M[i], 3))
        col3.append(round(ex3[i]/M[i], 3))
        col4.append(round(ex4[i]/M[i], 3))
    
    deltaX = (max(M)-min(M))
    
    grad_ex1 = (np.poly1d(np.polyfit(M, ex1, 1))(np.unique(M))[-1]-np.poly1d(np.polyfit(M, ex1, 1))(np.unique(M))[0])/deltaX
    grad_ex2 = (np.poly1d(np.polyfit(M, ex2, 1))(np.unique(M))[-1]-np.poly1d(np.polyfit(M, ex2, 1))(np.unique(M))[0])/deltaX
    grad_ex3 = (np.poly1d(np.polyfit(M, ex3, 1))(np.unique(M))[-1]-np.poly1d(np.polyfit(M, ex3, 1))(np.unique(M))[0])/deltaX
    grad_ex4 = (np.poly1d(np.polyfit(M, ex4, 1))(np.unique(M))[-1]-np.poly1d(np.polyfit(M, ex4, 1))(np.unique(M))[0])/deltaX
    
    pred_plot_y1 = [x*2e-06 for x in pred_plot_x]
    pred_plot_y2 = [x*3.63e-06 for x in pred_plot_x]
    pred_plot_y3 = [x*-2.28e-06 for x in pred_plot_x]
    pred_plot_y4 = [x*-3.69e-06 for x in pred_plot_x]

    
    plt.plot(M, ex1, 'b+', label = "Raw Data")
    plt.errorbar(pred_plot_x, pred_plot_y1, yerr = yerr4, fmt = "none", ecolor = "g")
    plt.plot(pred_plot_x, pred_plot_y1, "g-", label="Predicted")
    plt.xlabel("Load, N")
    plt.ylabel("Strain")
    plt.title("Gauge 1")
    plt.grid()
    plt.plot(np.unique(M), np.poly1d(np.polyfit(M, ex1, 1))(np.unique(M)), 'r-', label = "Best Fit")
    #plt.plot(pred_plot_x, pred_plot_y1, "r-", label = "Predicted")
    plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
    plt.legend(loc = "upper left")
    plt.savefig("Gauge1 graph.png")
    plt.show()
    
    plt.plot(M, ex2, 'b+', label = "Raw Data")
    plt.errorbar(pred_plot_x, pred_plot_y2, yerr = yerr4, fmt = "none", ecolor = "g")
    plt.plot(np.unique(M), np.poly1d(np.polyfit(M, ex2, 1))(np.unique(M)), 'r-', label = "Best Fit")
    plt.plot(pred_plot_x, pred_plot_y2, "g-", label = "Predicted")
    plt.xlabel("Load, N")
    plt.ylabel("Strain")
    plt.title("Gauge 2")
    plt.grid()
    plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
    plt.legend(loc = "upper left")
    plt.savefig("Gauge2 graph.png")
    plt.show()
    
    plt.plot(M, ex3, 'b+', label = "Raw Data")
    plt.errorbar(pred_plot_x, pred_plot_y3, yerr = yerr4, fmt = "none", ecolor = "g")
    plt.plot(np.unique(M), np.poly1d(np.polyfit(M, ex3, 1))(np.unique(M)), 'r-', label = "Best Fit")
    plt.plot(pred_plot_x, pred_plot_y3, "g-", label = "Predicted")
    plt.xlabel("Load, N")
    plt.ylabel("Strain")
    plt.title("Gauge 3")
    plt.grid()
    plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
    plt.legend()
    plt.savefig("Gauge3 graph.png")
    plt.show()
    
    plt.plot(M, ex4, 'b+', label = "Raw Data")
    plt.errorbar(pred_plot_x, pred_plot_y4, yerr = yerr4, fmt = "none", ecolor = "g")
    plt.plot(np.unique(M), np.poly1d(np.polyfit(M, ex4, 1))(np.unique(M)), 'r-', label = "Best Fit")
    plt.plot(pred_plot_x, pred_plot_y4, "g-", label = "Predicted")
    plt.xlabel("Load, N")
    plt.ylabel("Strain")
    plt.title("Gauge 4")
    plt.grid()
    #plt.errorbar(M, ex4, yerr4)
    plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
    plt.legend()
    plt.savefig("Gauge4 graph.png")
    plt.show()
        
    # round(sum(col1)/len(col1), 2), round(sum(col2)/len(col2), 2), round(sum(col3)/len(col3), 2), round(sum(col4)/len(col4), 2)
    return grad_ex1, grad_ex2, grad_ex3, grad_ex4


def alpha(Iy, Iz, Iyz):
    
    alpha1 = l_array[0]*(sum(Iy)*gauge_y[0]-sum(Iyz)*gauge_z[0])/(sum(Iy)*sum(Iz)-sum(Iyz)**2)
    alpha2 = l_array[1]*(sum(Iy)*gauge_y[1]-sum(Iyz)*gauge_z[1])/(sum(Iy)*sum(Iz)-sum(Iyz)**2)
    alpha3 = l_array[2]*(sum(Iy)*gauge_y[2]-sum(Iyz)*gauge_z[2])/(sum(Iy)*sum(Iz)-sum(Iyz)**2)
    alpha4 = l_array[3]*(sum(Iy)*gauge_y[3]-sum(Iyz)*gauge_z[3])/(sum(Iy)*sum(Iz)-sum(Iyz)**2)
    
    slopePred1 = -alpha1/E
    slopePred2 = -alpha2/E
    slopePred3 = -alpha3/E
    slopePred4 = -alpha4/E
    
    print("Alpha1 = " + str(alpha1))
    print("Alpha2 = " + str(alpha2))
    print("Alpha3 = " + str(alpha3))
    print("Alpha4 = " + str(alpha4))
    
    return slopePred1, slopePred2, slopePred3, slopePred4


def sigmaFromStrain(Iy, Iz, Iyz, ex1, ex2, ex3, ex4):
    """
    This makes use of equation 2.
    Use equation 3 instead!!!
    """
    sigma1 = []
    sigma2 = []
    sigma3 = []
    sigma4 = []
    
    ex1 = [x*10**(-6) for x in ex1]
    ex2 = [x*10**(-6) for x in ex2]
    ex3 = [x*10**(-6) for x in ex3]
    ex4 = [x*10**(-6) for x in ex4]
    
    M = [9.81*x for x in m_array]
    
    for i, P in enumerate(M):
        s1 = -((sum(Iy)*gauge_y[0]-sum(Iyz)*gauge_z[0])/(sum(Iy)*sum(Iz)-(sum(Iyz)**2)))*P*l_array[0]/ex1[i]
        s2 = -((sum(Iy)*gauge_y[1]-sum(Iyz)*gauge_z[1])/(sum(Iy)*sum(Iz)-(sum(Iyz)**2)))*P*l_array[1]/ex1[i]
        s3 = -((sum(Iy)*gauge_y[2]-sum(Iyz)*gauge_z[2])/(sum(Iy)*sum(Iz)-(sum(Iyz)**2)))*P*l_array[2]/ex1[i]
        s4 = -((sum(Iy)*gauge_y[3]-sum(Iyz)*gauge_z[3])/(sum(Iy)*sum(Iz)-(sum(Iyz)**2)))*P*l_array[3]/ex1[i]
        sigma1.append(s1)
        sigma2.append(s2)
        sigma3.append(s3)
        sigma4.append(s4)
    
    E1 = sum(sigma1)/len(sigma1)
    E2 = sum(sigma2)/len(sigma2)
    E3 = sum(sigma3)/len(sigma3)
    E4 = sum(sigma4)/len(sigma4)
    
    return E1, E2, E3, E4


def plotDeflectData(m_array, vb, wb):

    M = [9.81*x for x in m_array]
    
    plt.plot(M, vb, 'b+', label = "Raw Data")
    plt.plot(np.unique(M), np.poly1d(np.polyfit(M, vb, 1))(np.unique(M)), 'g-', label = "Best Fit")
    plt.title("Vertical Tip Deflection")
    plt.ylabel("Deflection, mm")
    plt.xlabel("Load, N")
    plt.grid(which = "major")
    plt.minorticks_on()
    plt.legend(loc = "upper left")
    plt.savefig("Verticle Deflection.png")
    plt.show()
    
    plt.plot(M, wb, 'b+', label = "Raw Data")
    plt.plot(np.unique(M), np.poly1d(np.polyfit(M, wb, 1))(np.unique(M)), 'g-', label = "Best Fit")
    plt.title("Horizontal Tip Deflection")
    plt.ylabel("Deflection, mm")
    plt.xlabel("Load, N")
    plt.grid(which = "major")
    plt.minorticks_on()
    plt.legend(loc = "upper left")
    plt.savefig("Horizontal Deflection.png")
    plt.show()
    
    plt.plot(vb, wb, "b+")
    plt.grid()
    plt.minorticks_on()
    plt.grid(which ="minor")
    plt.title("Comparison between Vertical and Horizontal \nDeflection")
    plt.xlabel("Vertical Deflection, mm")
    plt.ylabel("Horizontal Deflection, mm")
    plt.savefig("Deflection comparison.png")
    plt.show()
    
    deltaX = (max(M)-min(M))
    
    grad_vb = (np.poly1d(np.polyfit(M, vb, 1))(np.unique(M))[-1]-np.poly1d(np.polyfit(M, vb, 1))(np.unique(M))[0])/deltaX
    grad_wb = (np.poly1d(np.polyfit(M, wb, 1))(np.unique(M))[-1]-np.poly1d(np.polyfit(M, wb, 1))(np.unique(M))[0])/deltaX
    
    return round(grad_vb, 3), round(grad_wb, 3)
    

def beta(l_beam, Iy, Iz, Iyz, E):
    
    beta_v = ((l_beam**3)*sum(Iy))/(3*(sum(Iy)*sum(Iz)-(sum(Iyz)**2)))
    beta_w = (-(l_beam**3)*sum(Iyz))/(3*(sum(Iy)*sum(Iz)-(sum(Iyz)**2)))
    
    slopePred_vb = beta_v/E
    slopePred_wb = beta_w/E

    print(beta_v, beta_w)
    
    return round(slopePred_vb, 3), round(slopePred_wb, 3)
