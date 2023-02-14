#METABOLIC SYSTEM 3 EQUATION MODEL
using DelayDiffEq
using Statistics

function hill(k, i , w)
    return w^i/(k^i+w^i)
end

function system(du, u, h, p, t)
    row, kappa, n, A, B1, B2, B3, D1, D2, D3, Rt, tau3, tau1, tau2 = p
    histp12 = h(p, t-tau1)[2]
    histp13 = h(p, t-tau1)[3]
    histp21 = h(p, t-tau2)[1]
    histp31 = h(p, t-tau3)[1]
    histr1 = h(p, t-tau1)[4]
    histr2 = h(p, t-tau2)[4]
    histr3 = h(p, t-tau3)[4]
    
    du[1] = B1 * hill(kappa, n, histp12) * hill(kappa, n, histp13) * histr1 - D1 * u[1]
    du[2] = B2 * hill(kappa, n, histp21) * histr2 - D2 * u[2]
    du[3] = B3 * hill(kappa, n, histp31) * histr3 - D3 * u[3]
    du[4] = A * (hill(kappa, n, histp12) * hill(kappa, n, histp13) * histr1 +  hill(kappa, n, histp21) * histr2 + hill(kappa, n, histp31) * histr3 - hill(kappa, n, u[2]) * hill(kappa, n, u[3]) * u[4] - 2 * hill(kappa, n, u[1]) * u[4])
end

function trajectory(p, t_start, t_end)
    row = p["Row"]
    kappa = p["kappa"]
    n = p["n"]
    A = p["A"]
    B1 = p["B1"]
    B2 = p["B2"]
    B3 = p["B3"]
    D1 = p["B1"]
    D2 = p["D2"]
    D3 = p["D3"]
    Rt = p["Rt"]
    tau1 = p["tau1"]
    tau2 = p["tau2"]
    tau3 = p["tau3"]
    p = [row, kappa, n, A, B1, B2, B3, D1, D2, D3, Rt, tau3, tau1, tau2]
    u0 = initial_conditions(p)
    h(p,t) = u0
    alg = MethodOfSteps(Tsit5())
    tspan = (0.0,t_end)
    dt = 0.1
    num_points = floor(Int, (t_end-t_start)/dt)
    prob = DDEProblem(system, u0,h,tspan, p;constant_lags = [])
    sol = solve(prob,alg, abstol = 1e-8, reltol = 1e-8, adaptive=true)#, dt=delta_t)
    ts = range(t_start,stop=t_end, length=num_points)
    traj = [ts, sol(ts,idxs=1)[1,:], sol(ts,idxs=2)[1,:], sol(ts, idxs=3)[1,:], sol(ts, idxs=4)[1,:]]
    return traj
end

function initial_conditions(p)
    row, kappa, n, A, B1, B2, B3, D1, D2, D3, Rt, tau3, tau1, tau2 = p
    p10 = kappa
    p20 = kappa
    p30 = kappa
    taueq = 0.5*tau1 + tau2 + tau3
    R0 = 2 * Rt / (2 + A * taueq)
    u0 = [p10, p20, p30, R0]
    return u0
end
