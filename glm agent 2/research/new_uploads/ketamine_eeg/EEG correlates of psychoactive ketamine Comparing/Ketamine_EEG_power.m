%% EEG Correlates of Psychoactive Ketamine: Spectral Power and Complexity
% Author: Brandon Reynante
% Revision Date: 2026-02-03
% This code calculates spectral power of spontaneous EEG data during
% normal waking and psychoactive ketamine conditions with eyes closed

clear; clc; close all;

%% Load pre-processed EEG data
% From Farnes et al. (2020)

% Define relevant parameters
n_channels = 62;        % number of EEG channels
sampling_rate = 250;    % sampling rate (Hz)
n_samples = 2000;       % number of samples per epoch

% Load meta data (spontaneous EEG, eyes closed condition)
metadata_210_awake = load("-mat","../data/210_20161207_0003eyesClosed_afterICA.set");
metadata_219_awake = load("-mat","../data/219_20161117_0003_eyesClosed_afterICA.set");
metadata_249_awake = load("-mat","../data/249_20161208_0003EyesClosed_afterICA.set");
metadata_251_awake = load("-mat","../data/251_20170124_0003eyesClosed_afterICA.set");
metadata_265_awake = load("-mat","../data/265_20170112_0004_eyes_closed_afterICA.set");
metadata_271_awake = load("-mat","../data/271_20170221_0003eyesclosed_afterICA.set");
metadata_282_awake = load("-mat","../data/282_20161122_0003_eyesClosed_afterICA.set");
metadata_300_awake = load("-mat","../data/300_20161214_0003eyesClosed_afterICA.set");
metadata_313_awake = load("-mat","../data/313_20170116_0003EyesClosed_afterICA.set");
metadata_318_awake = load("-mat","../data/318_20170206_0003EyesClosed_afterICA.set");

metadata_210_ket = load("-mat","../data/210_20161207_0007eyesClosed_afterICA.set");
metadata_219_ket = load("-mat","../data/219_20161117_0007_closedEyes_afterICA.set");
metadata_249_ket = load("-mat","../data/249_20161208_0007eyesClosed_afterICA.set");
metadata_251_ket = load("-mat","../data/251_20170124_0007eyesClosed_afterICA.set");
metadata_265_ket = load("-mat","../data/265_20170112_0007eyesClosed_afterICA.set");
metadata_271_ket = load("-mat","../data/271_20170221_0007EyesClosed_afterICA.set");
metadata_282_ket = load("-mat","../data/282_20161122_0007_eyesClosed_afterICA.set");
metadata_300_ket = load("-mat","../data/300_20161214_0007eyesClosed_afterICA.set");
metadata_313_ket = load("-mat","../data/313_20170116_0007eyesClosed_afterICA.set");
metadata_318_ket = load("-mat","../data/318_20170206_0008EyesClosed_afterICA.set");

% Load raw data (spontaneous EEG, eyes closed condition)
fid = fopen("../data/210_20161207_0003eyesClosed_afterICA.fdt", "r");
eeg_210_awake = fread(fid,"*float"); fclose(fid);
fid = fopen("../data/219_20161117_0003_eyesClosed_afterICA.fdt", "r");
eeg_219_awake = fread(fid,"*float"); fclose(fid);
fid = fopen("../data/249_20161208_0003EyesClosed_afterICA.fdt", "r");
eeg_249_awake = fread(fid,"*float"); fclose(fid);
fid = fopen("../data/251_20170124_0003eyesClosed_afterICA.fdt", "r");
eeg_251_awake = fread(fid,"*float"); fclose(fid);
fid = fopen("../data/265_20170112_0004_eyes_closed_afterICA.fdt", "r");
eeg_265_awake = fread(fid,"*float"); fclose(fid);
fid = fopen("../data/271_20170221_0003eyesclosed_afterICA.fdt", "r");
eeg_271_awake = fread(fid,"*float"); fclose(fid);
fid = fopen("../data/282_20161122_0003_eyesClosed_afterICA.fdt", "r");
eeg_282_awake = fread(fid,"*float"); fclose(fid);
fid = fopen("../data/300_20161214_0003eyesClosed_afterICA.fdt", "r");
eeg_300_awake = fread(fid,"*float"); fclose(fid);
fid = fopen("../data/313_20170116_0003EyesClosed_afterICA.fdt", "r");
eeg_313_awake = fread(fid,"*float"); fclose(fid);
fid = fopen("../data/318_20170206_0003EyesClosed_afterICA.fdt", "r");
eeg_318_awake = fread(fid,"*float"); fclose(fid);

fid = fopen("../data/210_20161207_0007eyesClosed_afterICA.fdt", "r");
eeg_210_ket = fread(fid,"*float"); fclose(fid);
fid = fopen("../data/219_20161117_0007_closedEyes_afterICA.fdt", "r");
eeg_219_ket = fread(fid,"*float"); fclose(fid);
fid = fopen("../data/249_20161208_0007eyesClosed_afterICA.fdt", "r");
eeg_249_ket = fread(fid,"*float"); fclose(fid);
fid = fopen("../data/251_20170124_0007eyesClosed_afterICA.fdt", "r");
eeg_251_ket = fread(fid,"*float"); fclose(fid);
fid = fopen("../data/265_20170112_0007eyesClosed_afterICA.fdt", "r");
eeg_265_ket = fread(fid,"*float"); fclose(fid);
fid = fopen("../data/271_20170221_0007EyesClosed_afterICA.fdt", "r");
eeg_271_ket = fread(fid,"*float"); fclose(fid);
fid = fopen("../data/282_20161122_0007_eyesClosed_afterICA.fdt", "r");
eeg_282_ket = fread(fid,"*float"); fclose(fid);
fid = fopen("../data/300_20161214_0007eyesClosed_afterICA.fdt", "r");
eeg_300_ket = fread(fid,"*float"); fclose(fid);
fid = fopen("../data/313_20170116_0007eyesClosed_afterICA.fdt", "r");
eeg_313_ket = fread(fid,"*float"); fclose(fid);
fid = fopen("../data/318_20170206_0008EyesClosed_afterICA.fdt", "r");
eeg_318_ket = fread(fid,"*float"); fclose(fid);

% Shape the raw data into matrices with the dimensions of channels x samples
eeg_210_awake = reshape(eeg_210_awake,[n_channels,n_samples*metadata_210_awake.EEG.trials]);
eeg_219_awake = reshape(eeg_219_awake,[n_channels,n_samples*metadata_219_awake.EEG.trials]);
eeg_249_awake = reshape(eeg_249_awake,[n_channels,n_samples*metadata_249_awake.EEG.trials]);
eeg_251_awake = reshape(eeg_251_awake,[n_channels,n_samples*metadata_251_awake.EEG.trials]);
eeg_265_awake = reshape(eeg_265_awake,[n_channels,n_samples*metadata_265_awake.EEG.trials]);
eeg_271_awake = reshape(eeg_271_awake,[n_channels,n_samples*metadata_271_awake.EEG.trials]);
eeg_282_awake = reshape(eeg_282_awake,[n_channels,n_samples*metadata_282_awake.EEG.trials]);
eeg_300_awake = reshape(eeg_300_awake,[n_channels,n_samples*metadata_300_awake.EEG.trials]);
eeg_313_awake = reshape(eeg_313_awake,[n_channels,n_samples*metadata_313_awake.EEG.trials]);
eeg_318_awake = reshape(eeg_318_awake,[n_channels,n_samples*metadata_318_awake.EEG.trials]);

eeg_210_ket = reshape(eeg_210_ket,[n_channels,n_samples*metadata_210_ket.EEG.trials]);
eeg_219_ket = reshape(eeg_219_ket,[n_channels,n_samples*metadata_219_ket.EEG.trials]);
eeg_249_ket = reshape(eeg_249_ket,[n_channels,n_samples*metadata_249_ket.EEG.trials]);
eeg_251_ket = reshape(eeg_251_ket,[n_channels,n_samples*metadata_251_ket.EEG.trials]);
eeg_265_ket = reshape(eeg_265_ket,[n_channels,n_samples*metadata_265_ket.EEG.trials]);
eeg_271_ket = reshape(eeg_271_ket,[n_channels,n_samples*metadata_271_ket.EEG.trials]);
eeg_282_ket = reshape(eeg_282_ket,[n_channels,n_samples*metadata_282_ket.EEG.trials]);
eeg_300_ket = reshape(eeg_300_ket,[n_channels,n_samples*metadata_300_ket.EEG.trials]);
eeg_313_ket = reshape(eeg_313_ket,[n_channels,n_samples*metadata_313_ket.EEG.trials]);
eeg_318_ket = reshape(eeg_318_ket,[n_channels,n_samples*metadata_318_ket.EEG.trials]);

% Focus on specific channels for analysis (P6, Pz, P5, C6, Cz, C5, F6, Fz, F5)
eeg_210_awake = eeg_210_awake([11 14 17 31 34 37 49 52 55],:);
eeg_219_awake = eeg_219_awake([11 14 17 31 34 37 49 52 55],:);
eeg_249_awake = eeg_249_awake([11 14 17 31 34 37 49 52 55],:);
eeg_251_awake = eeg_251_awake([11 14 17 31 34 37 49 52 55],:);
eeg_265_awake = eeg_265_awake([11 14 17 31 34 37 49 52 55],:);
eeg_271_awake = eeg_271_awake([11 14 17 31 34 37 49 52 55],:);
eeg_282_awake = eeg_282_awake([11 14 17 31 34 37 49 52 55],:);
eeg_300_awake = eeg_300_awake([11 14 17 31 34 37 49 52 55],:);
eeg_313_awake = eeg_313_awake([11 14 17 31 34 37 49 52 55],:);
eeg_318_awake = eeg_318_awake([11 14 17 31 34 37 49 52 55],:);

eeg_210_ket = eeg_210_ket([11 14 17 31 34 37 49 52 55],:);
eeg_219_ket = eeg_219_ket([11 14 17 31 34 37 49 52 55],:);
eeg_249_ket = eeg_249_ket([11 14 17 31 34 37 49 52 55],:);
eeg_251_ket = eeg_251_ket([11 14 17 31 34 37 49 52 55],:);
eeg_265_ket = eeg_265_ket([11 14 17 31 34 37 49 52 55],:);
eeg_271_ket = eeg_271_ket([11 14 17 31 34 37 49 52 55],:);
eeg_282_ket = eeg_282_ket([11 14 17 31 34 37 49 52 55],:);
eeg_300_ket = eeg_300_ket([11 14 17 31 34 37 49 52 55],:);
eeg_313_ket = eeg_313_ket([11 14 17 31 34 37 49 52 55],:);
eeg_318_ket = eeg_318_ket([11 14 17 31 34 37 49 52 55],:);

%% Calculate spectral power

% Define spectral band frequency ranges in Hz
band_delta = [1 4];
band_theta = [4 8];
band_alpha = [8 12];
band_beta = [12 30];
band_gamma = [30 45];
band_combined = [band_delta;band_theta;band_alpha;band_beta;band_gamma];

% Define window length (sufficient to capture one full cycle of lowest frequency of interest)
window = (1/band_delta(1))*sampling_rate;

% Estimate the power spectral density at each EEG channel using Welch's method
[PSD_210_awake,F] = pwelch(eeg_210_awake',window,[],[],sampling_rate);
PSD_219_awake = pwelch(eeg_219_awake',window,[],[],sampling_rate);
PSD_249_awake = pwelch(eeg_249_awake',window,[],[],sampling_rate);
PSD_251_awake = pwelch(eeg_251_awake',window,[],[],sampling_rate);
PSD_265_awake = pwelch(eeg_265_awake',window,[],[],sampling_rate);
PSD_271_awake = pwelch(eeg_271_awake',window,[],[],sampling_rate);
PSD_282_awake = pwelch(eeg_282_awake',window,[],[],sampling_rate);
PSD_300_awake = pwelch(eeg_300_awake',window,[],[],sampling_rate);
PSD_313_awake = pwelch(eeg_313_awake',window,[],[],sampling_rate);
PSD_318_awake = pwelch(eeg_318_awake',window,[],[],sampling_rate);

PSD_210_ket = pwelch(eeg_210_ket',window,[],[],sampling_rate);
PSD_219_ket = pwelch(eeg_219_ket',window,[],[],sampling_rate);
PSD_249_ket = pwelch(eeg_249_ket',window,[],[],sampling_rate);
PSD_251_ket = pwelch(eeg_251_ket',window,[],[],sampling_rate);
PSD_265_ket = pwelch(eeg_265_ket',window,[],[],sampling_rate);
PSD_271_ket = pwelch(eeg_271_ket',window,[],[],sampling_rate);
PSD_282_ket = pwelch(eeg_282_ket',window,[],[],sampling_rate);
PSD_300_ket = pwelch(eeg_300_ket',window,[],[],sampling_rate);
PSD_313_ket = pwelch(eeg_313_ket',window,[],[],sampling_rate);
PSD_318_ket = pwelch(eeg_318_ket',window,[],[],sampling_rate);

% For each subject, compute average PSD across EEG channels
% For each condition, combine into a single matrix with all subjects
PSD_awake = [mean(PSD_210_awake,2)';
    mean(PSD_219_awake,2)';
    mean(PSD_249_awake,2)';
    mean(PSD_251_awake,2)';
    mean(PSD_265_awake,2)';
    mean(PSD_271_awake,2)';
    mean(PSD_282_awake,2)';
    mean(PSD_300_awake,2)';
    mean(PSD_313_awake,2)';
    mean(PSD_318_awake,2)'];

PSD_ket = [mean(PSD_210_ket,2)';
    mean(PSD_219_ket,2)';
    mean(PSD_249_ket,2)';
    mean(PSD_251_ket,2)';
    mean(PSD_265_ket,2)';
    mean(PSD_271_ket,2)';
    mean(PSD_282_ket,2)';
    mean(PSD_300_ket,2)';
    mean(PSD_313_ket,2)';
    mean(PSD_318_ket,2)'];

% Compute the logarithmic power spectral density
LPSD_210_awake = 10*log10(PSD_210_awake);
LPSD_219_awake = 10*log10(PSD_219_awake);
LPSD_249_awake = 10*log10(PSD_249_awake);
LPSD_251_awake = 10*log10(PSD_251_awake);
LPSD_265_awake = 10*log10(PSD_265_awake);
LPSD_271_awake = 10*log10(PSD_271_awake);
LPSD_282_awake = 10*log10(PSD_282_awake);
LPSD_300_awake = 10*log10(PSD_300_awake);
LPSD_313_awake = 10*log10(PSD_313_awake);
LPSD_318_awake = 10*log10(PSD_318_awake);

LPSD_210_ket = 10*log10(PSD_210_ket);
LPSD_219_ket = 10*log10(PSD_219_ket);
LPSD_249_ket = 10*log10(PSD_249_ket);
LPSD_251_ket = 10*log10(PSD_251_ket);
LPSD_265_ket = 10*log10(PSD_265_ket);
LPSD_271_ket = 10*log10(PSD_271_ket);
LPSD_282_ket = 10*log10(PSD_282_ket);
LPSD_300_ket = 10*log10(PSD_300_ket);
LPSD_313_ket = 10*log10(PSD_313_ket);
LPSD_318_ket = 10*log10(PSD_318_ket);

% For each subject, compute average LPSD across EEG channels
% For each condition, combine into a single matrix with all subjects
LPSD_awake = [mean(LPSD_210_awake,2)';
    mean(LPSD_219_awake,2)';
    mean(LPSD_249_awake,2)';
    mean(LPSD_251_awake,2)';
    mean(LPSD_265_awake,2)';
    mean(LPSD_271_awake,2)';
    mean(LPSD_282_awake,2)';
    mean(LPSD_300_awake,2)';
    mean(LPSD_313_awake,2)';
    mean(LPSD_318_awake,2)'];

LPSD_ket = [mean(LPSD_210_ket,2)';
    mean(LPSD_219_ket,2)';
    mean(LPSD_249_ket,2)';
    mean(LPSD_251_ket,2)';
    mean(LPSD_265_ket,2)';
    mean(LPSD_271_ket,2)';
    mean(LPSD_282_ket,2)';
    mean(LPSD_300_ket,2)';
    mean(LPSD_313_ket,2)';
    mean(LPSD_318_ket,2)'];

for index_power = 1:5 % loop over spectral bands
    
    % Find the indices corresponding to the frequency band of interest
    indices = find(F >= band_combined(index_power,1) & F <= band_combined(index_power,2));
    
    % Estimate spectral power at each channel by integrating the PSD within the desired frequency band via the trapezoidal method
    power_210_awake(index_power,:) = trapz(F(indices),PSD_210_awake(indices,:));
    power_219_awake(index_power,:) = trapz(F(indices),PSD_219_awake(indices,:));
    power_249_awake(index_power,:) = trapz(F(indices),PSD_249_awake(indices,:));
    power_251_awake(index_power,:) = trapz(F(indices),PSD_251_awake(indices,:));
    power_265_awake(index_power,:) = trapz(F(indices),PSD_265_awake(indices,:));
    power_271_awake(index_power,:) = trapz(F(indices),PSD_271_awake(indices,:));
    power_282_awake(index_power,:) = trapz(F(indices),PSD_282_awake(indices,:));
    power_300_awake(index_power,:) = trapz(F(indices),PSD_300_awake(indices,:));
    power_313_awake(index_power,:) = trapz(F(indices),PSD_313_awake(indices,:));
    power_318_awake(index_power,:) = trapz(F(indices),PSD_318_awake(indices,:));

    power_210_ket(index_power,:) = trapz(F(indices),PSD_210_ket(indices,:));
    power_219_ket(index_power,:) = trapz(F(indices),PSD_219_ket(indices,:));
    power_249_ket(index_power,:) = trapz(F(indices),PSD_249_ket(indices,:));
    power_251_ket(index_power,:) = trapz(F(indices),PSD_251_ket(indices,:));
    power_265_ket(index_power,:) = trapz(F(indices),PSD_265_ket(indices,:));
    power_271_ket(index_power,:) = trapz(F(indices),PSD_271_ket(indices,:));
    power_282_ket(index_power,:) = trapz(F(indices),PSD_282_ket(indices,:));
    power_300_ket(index_power,:) = trapz(F(indices),PSD_300_ket(indices,:));
    power_313_ket(index_power,:) = trapz(F(indices),PSD_313_ket(indices,:));
    power_318_ket(index_power,:) = trapz(F(indices),PSD_318_ket(indices,:));

end

% For each channel, compute average power across all subjects
% For each condition, combine into a single matrix with all channels
power_awake_P6 = [power_210_awake(:,1) power_219_awake(:,1) power_249_awake(:,1) power_251_awake(:,1) power_265_awake(:,1) power_271_awake(:,1) power_282_awake(:,1) power_300_awake(:,1) power_313_awake(:,1) power_318_awake(:,1)]';
power_awake_Pz = [power_210_awake(:,2) power_219_awake(:,2) power_249_awake(:,2) power_251_awake(:,2) power_265_awake(:,2) power_271_awake(:,2) power_282_awake(:,2) power_300_awake(:,2) power_313_awake(:,2) power_318_awake(:,2)]';
power_awake_P5 = [power_210_awake(:,3) power_219_awake(:,3) power_249_awake(:,3) power_251_awake(:,3) power_265_awake(:,3) power_271_awake(:,3) power_282_awake(:,3) power_300_awake(:,3) power_313_awake(:,3) power_318_awake(:,3)]';
power_awake_C6 = [power_210_awake(:,4) power_219_awake(:,4) power_249_awake(:,4) power_251_awake(:,4) power_265_awake(:,4) power_271_awake(:,4) power_282_awake(:,4) power_300_awake(:,4) power_313_awake(:,4) power_318_awake(:,4)]';
power_awake_Cz = [power_210_awake(:,5) power_219_awake(:,5) power_249_awake(:,5) power_251_awake(:,5) power_265_awake(:,5) power_271_awake(:,5) power_282_awake(:,5) power_300_awake(:,5) power_313_awake(:,5) power_318_awake(:,5)]';
power_awake_C5 = [power_210_awake(:,6) power_219_awake(:,6) power_249_awake(:,6) power_251_awake(:,6) power_265_awake(:,6) power_271_awake(:,6) power_282_awake(:,6) power_300_awake(:,6) power_313_awake(:,6) power_318_awake(:,6)]';
power_awake_F6 = [power_210_awake(:,7) power_219_awake(:,7) power_249_awake(:,7) power_251_awake(:,7) power_265_awake(:,7) power_271_awake(:,7) power_282_awake(:,7) power_300_awake(:,7) power_313_awake(:,7) power_318_awake(:,7)]';
power_awake_Fz = [power_210_awake(:,8) power_219_awake(:,8) power_249_awake(:,8) power_251_awake(:,8) power_265_awake(:,8) power_271_awake(:,8) power_282_awake(:,8) power_300_awake(:,8) power_313_awake(:,8) power_318_awake(:,8)]';
power_awake_F5 = [power_210_awake(:,9) power_219_awake(:,9) power_249_awake(:,9) power_251_awake(:,9) power_265_awake(:,9) power_271_awake(:,9) power_282_awake(:,9) power_300_awake(:,9) power_313_awake(:,9) power_318_awake(:,9)]';

power_ket_P6 = [power_210_ket(:,1) power_219_ket(:,1) power_249_ket(:,1) power_251_ket(:,1) power_265_ket(:,1) power_271_ket(:,1) power_282_ket(:,1) power_300_ket(:,1) power_313_ket(:,1) power_318_ket(:,1)]';
power_ket_Pz = [power_210_ket(:,2) power_219_ket(:,2) power_249_ket(:,2) power_251_ket(:,2) power_265_ket(:,2) power_271_ket(:,2) power_282_ket(:,2) power_300_ket(:,2) power_313_ket(:,2) power_318_ket(:,2)]';
power_ket_P5 = [power_210_ket(:,3) power_219_ket(:,3) power_249_ket(:,3) power_251_ket(:,3) power_265_ket(:,3) power_271_ket(:,3) power_282_ket(:,3) power_300_ket(:,3) power_313_ket(:,3) power_318_ket(:,3)]';
power_ket_C6 = [power_210_ket(:,4) power_219_ket(:,4) power_249_ket(:,4) power_251_ket(:,4) power_265_ket(:,4) power_271_ket(:,4) power_282_ket(:,4) power_300_ket(:,4) power_313_ket(:,4) power_318_ket(:,4)]';
power_ket_Cz = [power_210_ket(:,5) power_219_ket(:,5) power_249_ket(:,5) power_251_ket(:,5) power_265_ket(:,5) power_271_ket(:,5) power_282_ket(:,5) power_300_ket(:,5) power_313_ket(:,5) power_318_ket(:,5)]';
power_ket_C5 = [power_210_ket(:,6) power_219_ket(:,6) power_249_ket(:,6) power_251_ket(:,6) power_265_ket(:,6) power_271_ket(:,6) power_282_ket(:,6) power_300_ket(:,6) power_313_ket(:,6) power_318_ket(:,6)]';
power_ket_F6 = [power_210_ket(:,7) power_219_ket(:,7) power_249_ket(:,7) power_251_ket(:,7) power_265_ket(:,7) power_271_ket(:,7) power_282_ket(:,7) power_300_ket(:,7) power_313_ket(:,7) power_318_ket(:,7)]';
power_ket_Fz = [power_210_ket(:,8) power_219_ket(:,8) power_249_ket(:,8) power_251_ket(:,8) power_265_ket(:,8) power_271_ket(:,8) power_282_ket(:,8) power_300_ket(:,8) power_313_ket(:,8) power_318_ket(:,8)]';
power_ket_F5 = [power_210_ket(:,9) power_219_ket(:,9) power_249_ket(:,9) power_251_ket(:,9) power_265_ket(:,9) power_271_ket(:,9) power_282_ket(:,9) power_300_ket(:,9) power_313_ket(:,9) power_318_ket(:,9)]';

% For each subject, compute average power across all channels
% For each condition, combine into a single matrix with all subjects
power_awake = [mean(power_210_awake,2)';
    mean(power_219_awake,2)';
    mean(power_249_awake,2)';
    mean(power_251_awake,2)';
    mean(power_265_awake,2)';
    mean(power_271_awake,2)';
    mean(power_282_awake,2)';
    mean(power_300_awake,2)';
    mean(power_313_awake,2)';
    mean(power_318_awake,2)'];

power_ket = [mean(power_210_ket,2)';
    mean(power_219_ket,2)';
    mean(power_249_ket,2)';
    mean(power_251_ket,2)';
    mean(power_265_ket,2)';
    mean(power_271_ket,2)';
    mean(power_282_ket,2)';
    mean(power_300_ket,2)';
    mean(power_313_ket,2)';
    mean(power_318_ket,2)'];

%% Perform statistical analyses

% Calculate standard error of the mean (SEM) for PSD and LPSD
n_subjects = length(PSD_awake(:,1));
CI95 = tinv([0.025 0.975], n_subjects-1);

PSD_awake_mean = mean(PSD_awake,1);
PSD_awake_SEM = std(PSD_awake,1) / sqrt(n_subjects);
PSD_awake_lower = PSD_awake_mean - PSD_awake_SEM;
PSD_awake_upper = PSD_awake_mean + PSD_awake_SEM;

PSD_ket_mean = mean(PSD_ket,1);
PSD_ket_SEM = std(PSD_ket,1) / sqrt(n_subjects);
PSD_ket_lower = PSD_ket_mean - PSD_ket_SEM;
PSD_ket_upper = PSD_ket_mean + PSD_ket_SEM;

LPSD_awake_mean = mean(LPSD_awake,1);
LPSD_awake_SEM = std(LPSD_awake,1) / sqrt(n_subjects);
LPSD_awake_lower = LPSD_awake_mean - LPSD_awake_SEM;
LPSD_awake_upper = LPSD_awake_mean + LPSD_awake_SEM;

LPSD_ket_mean = mean(LPSD_ket,1);
LPSD_ket_SEM = std(LPSD_ket,1) / sqrt(n_subjects);
LPSD_ket_lower = LPSD_ket_mean - LPSD_ket_SEM;
LPSD_ket_upper = LPSD_ket_mean + LPSD_ket_SEM;

% Compute effect sizes (Cohen's d) for total spectral power
effect_size_delta = meanEffectSize(power_awake(:,1),power_ket(:,1),Paired=true,Effect="cohen",Alpha=0.05);
effect_size_delta_P6 = meanEffectSize(power_awake_P6(:,1),power_ket_P6(:,1),Paired=true,Effect="cohen",Alpha=0.05);
effect_size_delta_Pz = meanEffectSize(power_awake_Pz(:,1),power_ket_Pz(:,1),Paired=true,Effect="cohen",Alpha=0.05);
effect_size_delta_P5 = meanEffectSize(power_awake_P5(:,1),power_ket_P5(:,1),Paired=true,Effect="cohen",Alpha=0.05);
effect_size_delta_C6 = meanEffectSize(power_awake_C6(:,1),power_ket_C6(:,1),Paired=true,Effect="cohen",Alpha=0.05);
effect_size_delta_Cz = meanEffectSize(power_awake_Cz(:,1),power_ket_Cz(:,1),Paired=true,Effect="cohen",Alpha=0.05);
effect_size_delta_C5 = meanEffectSize(power_awake_C5(:,1),power_ket_C5(:,1),Paired=true,Effect="cohen",Alpha=0.05);
effect_size_delta_F6 = meanEffectSize(power_awake_F6(:,1),power_ket_F6(:,1),Paired=true,Effect="cohen",Alpha=0.05);
effect_size_delta_Fz = meanEffectSize(power_awake_Fz(:,1),power_ket_Fz(:,1),Paired=true,Effect="cohen",Alpha=0.05);
effect_size_delta_F5 = meanEffectSize(power_awake_F5(:,1),power_ket_F5(:,1),Paired=true,Effect="cohen",Alpha=0.05);
effect_size_delta_all = double([effect_size_delta_P6{:,1},effect_size_delta_Pz{:,1},effect_size_delta_P5{:,1},effect_size_delta_C6{:,1},effect_size_delta_Cz{:,1},effect_size_delta_C5{:,1},effect_size_delta_F6{:,1},effect_size_delta_Fz{:,1},effect_size_delta_F5{:,1}]);

effect_size_theta = meanEffectSize(power_awake(:,2),power_ket(:,2),Paired=true,Effect="cohen",Alpha=0.05);
effect_size_theta_P6 = meanEffectSize(power_awake_P6(:,2),power_ket_P6(:,2),Paired=true,Effect="cohen",Alpha=0.05);
effect_size_theta_Pz = meanEffectSize(power_awake_Pz(:,2),power_ket_Pz(:,2),Paired=true,Effect="cohen",Alpha=0.05);
effect_size_theta_P5 = meanEffectSize(power_awake_P5(:,2),power_ket_P5(:,2),Paired=true,Effect="cohen",Alpha=0.05);
effect_size_theta_C6 = meanEffectSize(power_awake_C6(:,2),power_ket_C6(:,2),Paired=true,Effect="cohen",Alpha=0.05);
effect_size_theta_Cz = meanEffectSize(power_awake_Cz(:,2),power_ket_Cz(:,2),Paired=true,Effect="cohen",Alpha=0.05);
effect_size_theta_C5 = meanEffectSize(power_awake_C5(:,2),power_ket_C5(:,2),Paired=true,Effect="cohen",Alpha=0.05);
effect_size_theta_F6 = meanEffectSize(power_awake_F6(:,2),power_ket_F6(:,2),Paired=true,Effect="cohen",Alpha=0.05);
effect_size_theta_Fz = meanEffectSize(power_awake_Fz(:,2),power_ket_Fz(:,2),Paired=true,Effect="cohen",Alpha=0.05);
effect_size_theta_F5 = meanEffectSize(power_awake_F5(:,2),power_ket_F5(:,2),Paired=true,Effect="cohen",Alpha=0.05);
effect_size_theta_all = double([effect_size_theta_P6{:,1},effect_size_theta_Pz{:,1},effect_size_theta_P5{:,1},effect_size_theta_C6{:,1},effect_size_theta_Cz{:,1},effect_size_theta_C5{:,1},effect_size_theta_F6{:,1},effect_size_theta_Fz{:,1},effect_size_theta_F5{:,1}]);

effect_size_alpha = meanEffectSize(power_awake(:,3),power_ket(:,3),Paired=true,Effect="cohen",Alpha=0.05);
effect_size_alpha_P6 = meanEffectSize(power_awake_P6(:,3),power_ket_P6(:,3),Paired=true,Effect="cohen",Alpha=0.05);
effect_size_alpha_Pz = meanEffectSize(power_awake_Pz(:,3),power_ket_Pz(:,3),Paired=true,Effect="cohen",Alpha=0.05);
effect_size_alpha_P5 = meanEffectSize(power_awake_P5(:,3),power_ket_P5(:,3),Paired=true,Effect="cohen",Alpha=0.05);
effect_size_alpha_C6 = meanEffectSize(power_awake_C6(:,3),power_ket_C6(:,3),Paired=true,Effect="cohen",Alpha=0.05);
effect_size_alpha_Cz = meanEffectSize(power_awake_Cz(:,3),power_ket_Cz(:,3),Paired=true,Effect="cohen",Alpha=0.05);
effect_size_alpha_C5 = meanEffectSize(power_awake_C5(:,3),power_ket_C5(:,3),Paired=true,Effect="cohen",Alpha=0.05);
effect_size_alpha_F6 = meanEffectSize(power_awake_F6(:,3),power_ket_F6(:,3),Paired=true,Effect="cohen",Alpha=0.05);
effect_size_alpha_Fz = meanEffectSize(power_awake_Fz(:,3),power_ket_Fz(:,3),Paired=true,Effect="cohen",Alpha=0.05);
effect_size_alpha_F5 = meanEffectSize(power_awake_F5(:,3),power_ket_F5(:,3),Paired=true,Effect="cohen",Alpha=0.05);
effect_size_alpha_all = double([effect_size_alpha_P6{:,1},effect_size_alpha_Pz{:,1},effect_size_alpha_P5{:,1},effect_size_alpha_C6{:,1},effect_size_alpha_Cz{:,1},effect_size_alpha_C5{:,1},effect_size_alpha_F6{:,1},effect_size_alpha_Fz{:,1},effect_size_alpha_F5{:,1}]);

effect_size_beta = meanEffectSize(power_awake(:,4),power_ket(:,4),Paired=true,Effect="cohen",Alpha=0.05);
effect_size_beta_P6 = meanEffectSize(power_awake_P6(:,4),power_ket_P6(:,4),Paired=true,Effect="cohen",Alpha=0.05);
effect_size_beta_Pz = meanEffectSize(power_awake_Pz(:,4),power_ket_Pz(:,4),Paired=true,Effect="cohen",Alpha=0.05);
effect_size_beta_P5 = meanEffectSize(power_awake_P5(:,4),power_ket_P5(:,4),Paired=true,Effect="cohen",Alpha=0.05);
effect_size_beta_C6 = meanEffectSize(power_awake_C6(:,4),power_ket_C6(:,4),Paired=true,Effect="cohen",Alpha=0.05);
effect_size_beta_Cz = meanEffectSize(power_awake_Cz(:,4),power_ket_Cz(:,4),Paired=true,Effect="cohen",Alpha=0.05);
effect_size_beta_C5 = meanEffectSize(power_awake_C5(:,4),power_ket_C5(:,4),Paired=true,Effect="cohen",Alpha=0.05);
effect_size_beta_F6 = meanEffectSize(power_awake_F6(:,4),power_ket_F6(:,4),Paired=true,Effect="cohen",Alpha=0.05);
effect_size_beta_Fz = meanEffectSize(power_awake_Fz(:,4),power_ket_Fz(:,4),Paired=true,Effect="cohen",Alpha=0.05);
effect_size_beta_F5 = meanEffectSize(power_awake_F5(:,4),power_ket_F5(:,4),Paired=true,Effect="cohen",Alpha=0.05);
effect_size_beta_all = double([effect_size_beta_P6{:,1},effect_size_beta_Pz{:,1},effect_size_beta_P5{:,1},effect_size_beta_C6{:,1},effect_size_beta_Cz{:,1},effect_size_beta_C5{:,1},effect_size_beta_F6{:,1},effect_size_beta_Fz{:,1},effect_size_beta_F5{:,1}]);

effect_size_gamma = meanEffectSize(power_awake(:,5),power_ket(:,5),Paired=true,Effect="cohen",Alpha=0.05);
effect_size_gamma_P6 = meanEffectSize(power_awake_P6(:,5),power_ket_P6(:,5),Paired=true,Effect="cohen",Alpha=0.05);
effect_size_gamma_Pz = meanEffectSize(power_awake_Pz(:,5),power_ket_Pz(:,5),Paired=true,Effect="cohen",Alpha=0.05);
effect_size_gamma_P5 = meanEffectSize(power_awake_P5(:,5),power_ket_P5(:,5),Paired=true,Effect="cohen",Alpha=0.05);
effect_size_gamma_C6 = meanEffectSize(power_awake_C6(:,5),power_ket_C6(:,5),Paired=true,Effect="cohen",Alpha=0.05);
effect_size_gamma_Cz = meanEffectSize(power_awake_Cz(:,5),power_ket_Cz(:,5),Paired=true,Effect="cohen",Alpha=0.05);
effect_size_gamma_C5 = meanEffectSize(power_awake_C5(:,5),power_ket_C5(:,5),Paired=true,Effect="cohen",Alpha=0.05);
effect_size_gamma_F6 = meanEffectSize(power_awake_F6(:,5),power_ket_F6(:,5),Paired=true,Effect="cohen",Alpha=0.05);
effect_size_gamma_Fz = meanEffectSize(power_awake_Fz(:,5),power_ket_Fz(:,5),Paired=true,Effect="cohen",Alpha=0.05);
effect_size_gamma_F5 = meanEffectSize(power_awake_F5(:,5),power_ket_F5(:,5),Paired=true,Effect="cohen",Alpha=0.05);
effect_size_gamma_all = double([effect_size_gamma_P6{:,1},effect_size_gamma_Pz{:,1},effect_size_gamma_P5{:,1},effect_size_gamma_C6{:,1},effect_size_gamma_Cz{:,1},effect_size_gamma_C5{:,1},effect_size_gamma_F6{:,1},effect_size_gamma_Fz{:,1},effect_size_gamma_F5{:,1}]);

%% Visualize results

% PSD and LPSD (averaged across subjects)
figure
tiledlayout("vertical")

nexttile
hold on
plot(F',PSD_awake_mean)
fill([F' fliplr(F')],[PSD_awake_upper fliplr(PSD_awake_lower)],'b','EdgeColor','none','FaceAlpha',0.20)
plot(F',PSD_ket_mean)
fill([F' fliplr(F')],[PSD_ket_upper fliplr(PSD_ket_lower)],'r','EdgeColor','none','FaceAlpha',0.20)
xline([band_delta(1) band_delta(2) band_theta(2) band_alpha(2) band_beta(2) band_gamma(2)], '--')
ax = gca; ax.FontSize = 12; set(gca,'Box','on'); xlim([0 45]);
xlabel('Frequency (Hz)')
ylabel('PSD (\muV^2 / Hz)')
legend('Awake (mean)','Awake (SEM)','Ketamine (mean)','Ketamine (SEM)')

nexttile
hold on
plot(F',LPSD_awake_mean)
fill([F' fliplr(F')],[LPSD_awake_upper fliplr(LPSD_awake_lower)],'b','EdgeColor','none','FaceAlpha',0.20)
plot(F',LPSD_ket_mean)
fill([F' fliplr(F')],[LPSD_ket_upper fliplr(LPSD_ket_lower)],'r','EdgeColor','none','FaceAlpha',0.20)
xline([band_delta(1) band_delta(2) band_theta(2) band_alpha(2) band_beta(2) band_gamma(2)], '--')
ax = gca; ax.FontSize = 12; set(gca,'Box','on'); xlim([0 45]);
xlabel('Frequency (Hz)')
ylabel('LPSD (dB / Hz)')
legend('Awake (mean)','Awake (SEM)','Ketamine (mean)','Ketamine (SEM)')

%% Export data

writematrix(power_awake, 'power_awake.csv')
writematrix(power_ket, 'power_ket.csv')

writematrix([effect_size_delta_F5{:,"Effect"}, effect_size_delta_F5{:,"ConfidenceIntervals"}(:,1), effect_size_delta_F5{:,"ConfidenceIntervals"}(:,2);
    effect_size_delta_Fz{:,"Effect"}, effect_size_delta_Fz{:,"ConfidenceIntervals"}(:,1), effect_size_delta_Fz{:,"ConfidenceIntervals"}(:,2);
    effect_size_delta_F6{:,"Effect"}, effect_size_delta_F6{:,"ConfidenceIntervals"}(:,1), effect_size_delta_F6{:,"ConfidenceIntervals"}(:,2);
    effect_size_delta_C5{:,"Effect"}, effect_size_delta_C5{:,"ConfidenceIntervals"}(:,1), effect_size_delta_C5{:,"ConfidenceIntervals"}(:,2);
    effect_size_delta_Cz{:,"Effect"}, effect_size_delta_Cz{:,"ConfidenceIntervals"}(:,1), effect_size_delta_Cz{:,"ConfidenceIntervals"}(:,2);
    effect_size_delta_C6{:,"Effect"}, effect_size_delta_C6{:,"ConfidenceIntervals"}(:,1), effect_size_delta_C6{:,"ConfidenceIntervals"}(:,2);
    effect_size_delta_P5{:,"Effect"}, effect_size_delta_P5{:,"ConfidenceIntervals"}(:,1), effect_size_delta_P5{:,"ConfidenceIntervals"}(:,2);
    effect_size_delta_Pz{:,"Effect"}, effect_size_delta_Pz{:,"ConfidenceIntervals"}(:,1), effect_size_delta_Pz{:,"ConfidenceIntervals"}(:,2);
    effect_size_delta_P6{:,"Effect"}, effect_size_delta_P6{:,"ConfidenceIntervals"}(:,1), effect_size_delta_P6{:,"ConfidenceIntervals"}(:,2);
    effect_size_delta{:,"Effect"}, effect_size_delta{:,"ConfidenceIntervals"}(:,1), effect_size_delta{:,"ConfidenceIntervals"}(:,2);], 'effect_size_delta.csv');

writematrix([effect_size_theta_F5{:,"Effect"}, effect_size_theta_F5{:,"ConfidenceIntervals"}(:,1), effect_size_theta_F5{:,"ConfidenceIntervals"}(:,2);
    effect_size_theta_Fz{:,"Effect"}, effect_size_theta_Fz{:,"ConfidenceIntervals"}(:,1), effect_size_theta_Fz{:,"ConfidenceIntervals"}(:,2);
    effect_size_theta_F6{:,"Effect"}, effect_size_theta_F6{:,"ConfidenceIntervals"}(:,1), effect_size_theta_F6{:,"ConfidenceIntervals"}(:,2);
    effect_size_theta_C5{:,"Effect"}, effect_size_theta_C5{:,"ConfidenceIntervals"}(:,1), effect_size_theta_C5{:,"ConfidenceIntervals"}(:,2);
    effect_size_theta_Cz{:,"Effect"}, effect_size_theta_Cz{:,"ConfidenceIntervals"}(:,1), effect_size_theta_Cz{:,"ConfidenceIntervals"}(:,2);
    effect_size_theta_C6{:,"Effect"}, effect_size_theta_C6{:,"ConfidenceIntervals"}(:,1), effect_size_theta_C6{:,"ConfidenceIntervals"}(:,2);
    effect_size_theta_P5{:,"Effect"}, effect_size_theta_P5{:,"ConfidenceIntervals"}(:,1), effect_size_theta_P5{:,"ConfidenceIntervals"}(:,2);
    effect_size_theta_Pz{:,"Effect"}, effect_size_theta_Pz{:,"ConfidenceIntervals"}(:,1), effect_size_theta_Pz{:,"ConfidenceIntervals"}(:,2);
    effect_size_theta_P6{:,"Effect"}, effect_size_theta_P6{:,"ConfidenceIntervals"}(:,1), effect_size_theta_P6{:,"ConfidenceIntervals"}(:,2);
    effect_size_theta{:,"Effect"}, effect_size_theta{:,"ConfidenceIntervals"}(:,1), effect_size_theta{:,"ConfidenceIntervals"}(:,2)], 'effect_size_theta.csv');

writematrix([effect_size_alpha_F5{:,"Effect"}, effect_size_alpha_F5{:,"ConfidenceIntervals"}(:,1), effect_size_alpha_F5{:,"ConfidenceIntervals"}(:,2);
    effect_size_alpha_Fz{:,"Effect"}, effect_size_alpha_Fz{:,"ConfidenceIntervals"}(:,1), effect_size_alpha_Fz{:,"ConfidenceIntervals"}(:,2);
    effect_size_alpha_F6{:,"Effect"}, effect_size_alpha_F6{:,"ConfidenceIntervals"}(:,1), effect_size_alpha_F6{:,"ConfidenceIntervals"}(:,2);
    effect_size_alpha_C5{:,"Effect"}, effect_size_alpha_C5{:,"ConfidenceIntervals"}(:,1), effect_size_alpha_C5{:,"ConfidenceIntervals"}(:,2);
    effect_size_alpha_Cz{:,"Effect"}, effect_size_alpha_Cz{:,"ConfidenceIntervals"}(:,1), effect_size_alpha_Cz{:,"ConfidenceIntervals"}(:,2);
    effect_size_alpha_C6{:,"Effect"}, effect_size_alpha_C6{:,"ConfidenceIntervals"}(:,1), effect_size_alpha_C6{:,"ConfidenceIntervals"}(:,2);
    effect_size_alpha_P5{:,"Effect"}, effect_size_alpha_P5{:,"ConfidenceIntervals"}(:,1), effect_size_alpha_P5{:,"ConfidenceIntervals"}(:,2);
    effect_size_alpha_Pz{:,"Effect"}, effect_size_alpha_Pz{:,"ConfidenceIntervals"}(:,1), effect_size_alpha_Pz{:,"ConfidenceIntervals"}(:,2);
    effect_size_alpha_P6{:,"Effect"}, effect_size_alpha_P6{:,"ConfidenceIntervals"}(:,1), effect_size_alpha_P6{:,"ConfidenceIntervals"}(:,2);
    effect_size_alpha{:,"Effect"}, effect_size_alpha{:,"ConfidenceIntervals"}(:,1), effect_size_alpha{:,"ConfidenceIntervals"}(:,2)], 'effect_size_alpha.csv');

writematrix([effect_size_beta_F5{:,"Effect"}, effect_size_beta_F5{:,"ConfidenceIntervals"}(:,1), effect_size_beta_F5{:,"ConfidenceIntervals"}(:,2);
    effect_size_beta_Fz{:,"Effect"}, effect_size_beta_Fz{:,"ConfidenceIntervals"}(:,1), effect_size_beta_Fz{:,"ConfidenceIntervals"}(:,2);
    effect_size_beta_F6{:,"Effect"}, effect_size_beta_F6{:,"ConfidenceIntervals"}(:,1), effect_size_beta_F6{:,"ConfidenceIntervals"}(:,2);
    effect_size_beta_C5{:,"Effect"}, effect_size_beta_C5{:,"ConfidenceIntervals"}(:,1), effect_size_beta_C5{:,"ConfidenceIntervals"}(:,2);
    effect_size_beta_Cz{:,"Effect"}, effect_size_beta_Cz{:,"ConfidenceIntervals"}(:,1), effect_size_beta_Cz{:,"ConfidenceIntervals"}(:,2);
    effect_size_beta_C6{:,"Effect"}, effect_size_beta_C6{:,"ConfidenceIntervals"}(:,1), effect_size_beta_C6{:,"ConfidenceIntervals"}(:,2);
    effect_size_beta_P5{:,"Effect"}, effect_size_beta_P5{:,"ConfidenceIntervals"}(:,1), effect_size_beta_P5{:,"ConfidenceIntervals"}(:,2);
    effect_size_beta_Pz{:,"Effect"}, effect_size_beta_Pz{:,"ConfidenceIntervals"}(:,1), effect_size_beta_Pz{:,"ConfidenceIntervals"}(:,2);
    effect_size_beta_P6{:,"Effect"}, effect_size_beta_P6{:,"ConfidenceIntervals"}(:,1), effect_size_beta_P6{:,"ConfidenceIntervals"}(:,2);
    effect_size_beta{:,"Effect"}, effect_size_beta{:,"ConfidenceIntervals"}(:,1), effect_size_beta{:,"ConfidenceIntervals"}(:,2)], 'effect_size_beta.csv');

writematrix([effect_size_gamma_F5{:,"Effect"}, effect_size_gamma_F5{:,"ConfidenceIntervals"}(:,1), effect_size_gamma_F5{:,"ConfidenceIntervals"}(:,2);
    effect_size_gamma_Fz{:,"Effect"}, effect_size_gamma_Fz{:,"ConfidenceIntervals"}(:,1), effect_size_gamma_Fz{:,"ConfidenceIntervals"}(:,2);
    effect_size_gamma_F6{:,"Effect"}, effect_size_gamma_F6{:,"ConfidenceIntervals"}(:,1), effect_size_gamma_F6{:,"ConfidenceIntervals"}(:,2);
    effect_size_gamma_C5{:,"Effect"}, effect_size_gamma_C5{:,"ConfidenceIntervals"}(:,1), effect_size_gamma_C5{:,"ConfidenceIntervals"}(:,2);
    effect_size_gamma_Cz{:,"Effect"}, effect_size_gamma_Cz{:,"ConfidenceIntervals"}(:,1), effect_size_gamma_Cz{:,"ConfidenceIntervals"}(:,2);
    effect_size_gamma_C6{:,"Effect"}, effect_size_gamma_C6{:,"ConfidenceIntervals"}(:,1), effect_size_gamma_C6{:,"ConfidenceIntervals"}(:,2);
    effect_size_gamma_P5{:,"Effect"}, effect_size_gamma_P5{:,"ConfidenceIntervals"}(:,1), effect_size_gamma_P5{:,"ConfidenceIntervals"}(:,2);
    effect_size_gamma_Pz{:,"Effect"}, effect_size_gamma_Pz{:,"ConfidenceIntervals"}(:,1), effect_size_gamma_Pz{:,"ConfidenceIntervals"}(:,2);
    effect_size_gamma_P6{:,"Effect"}, effect_size_gamma_P6{:,"ConfidenceIntervals"}(:,1), effect_size_gamma_P6{:,"ConfidenceIntervals"}(:,2);
    effect_size_gamma{:,"Effect"}, effect_size_gamma{:,"ConfidenceIntervals"}(:,1), effect_size_gamma{:,"ConfidenceIntervals"}(:,2)], 'effect_size_gamma.csv');