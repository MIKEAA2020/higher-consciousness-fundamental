%% EEG Correlates of Psychoactive Ketamine: Spectral Power and Complexity
% Author: Brandon Reynante
% Revision Date: 2026-02-04
% This code calculates the correlations between 11D-ASC scores and changes 
% in EEG spectral power and complexity

clear; clc; close all;

%% Load data

% Load 11D-ASC scores
ASC = readmatrix('../Data/11D-ASC.csv');
ASC = [ASC; mean(ASC,1)]';

% Load data for whole-brain EEG spectral power and complexity
power_awake = readmatrix('../Data/power_awake.csv');
power_ket = readmatrix('../Data/power_ket.csv');
complexity_awake = readmatrix('../Data/complexity_awake.csv');
complexity_ket = readmatrix('../Data/complexity_ket.csv');

% Compute difference between conditions for power and complexity
power_diff = power_ket - power_awake;
complexity_diff = complexity_ket - complexity_awake;

%% Test data for normality using the Anderson-Darling test

% ASC scores
for index1 = size(ASC,2)
    h_ASC(index1) = adtest(ASC(:,index1));
end

% Spectral power
for index1 = size(power_diff,2)
    h_power_diff(index1) = adtest(power_diff(:,index1));
end

% Complexity
for index1 = size(complexity_diff,2)
    h_complexity_diff(index1) = adtest(complexity_diff(:,index1));
end

%% Calculate correlations

% Pearson correlation
A = [ASC power_diff complexity_diff];
[rho,pval,rho_lo,rho_up] = corrcoef(A);

% Extract relevant sections of correlation matrices
Rho = rho(13:19,1:12);
Rho_lo = rho_lo(13:19,1:12);
Rho_up = rho_up(13:19,1:12);

% Identify strong correlations
rho_cutoff = 0.5; % define cutoff level for strong rho values
[rho_strong_row,rho_strong_col] = find(abs(Rho) > rho_cutoff);
linear_indices = sub2ind(size(Rho), rho_strong_row, rho_strong_col);
rho_strong = Rho(linear_indices);
rho_lo_strong = Rho_lo(linear_indices);
rho_up_strong = Rho_up(linear_indices);

%% Export files

writematrix(Rho,'rho.csv');
writematrix([rho_strong rho_lo_strong rho_up_strong],'rho_strong.csv');