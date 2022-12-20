# #Duffing Oscillator
using DifferentialEquations
using Statistics

function system(du, u, p, t)
    row, d, alpha, x0, y0 = p
    du[1] = u[2]
    du[2] = -alpha*u[1] - u[1]^3 - d * u[2]
end


function trajectory(p, t_start, t_end)
    row, d, alpha, x0, y0 = p
    u0 = [x0, y0]
#     alg = MethodOfSteps(Tsit5())
    tspan = (0.0,t_end)
    dt = 0.1
    num_points = floor(Int, (t_end-t_start)/dt)
    prob = ODEProblem(system,u0,tspan, p)
    sol = solve(prob,Tsit5(), abstol = 1e-10, reltol = 1e-10)
    ts = range(t_start, stop=t_end, length=num_points)
    traj = [ts, sol(ts,idxs=1)[1,:], sol(ts,idxs=2)[1,:]]
    return traj
end

