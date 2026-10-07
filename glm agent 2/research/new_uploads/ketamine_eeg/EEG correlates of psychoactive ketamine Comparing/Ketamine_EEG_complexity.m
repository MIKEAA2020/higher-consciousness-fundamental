%% EEG Correlates of Psychoactive Ketamine: Spectral Power and Complexity
% Author: Brandon Reynante
% Revision Date: 2026-02-02
% This code calculates neural signal complexity of spontaneous EEG during
% normal waking and psychoactive ketamine conditions with eyes closed

clear; clc; close all;

%% Load pre-processed EEG data
% From Farnes et al. (2020)

% Define relevant parameters
sampling_rate = 250;    % sampling rate (Hz)
n_channels = 62;        % number of EEG channels
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

%% Calculate Lempel-Ziv-Welch complexity

% Obtain instantaneous EEG signal amplitude using the Hilbert transform
eeg_amp_210_awake = abs(hilbert(eeg_210_awake));
eeg_amp_219_awake = abs(hilbert(eeg_219_awake));
eeg_amp_249_awake = abs(hilbert(eeg_249_awake));
eeg_amp_251_awake = abs(hilbert(eeg_251_awake));
eeg_amp_265_awake = abs(hilbert(eeg_265_awake));
eeg_amp_271_awake = abs(hilbert(eeg_271_awake));
eeg_amp_282_awake = abs(hilbert(eeg_282_awake));
eeg_amp_300_awake = abs(hilbert(eeg_300_awake));
eeg_amp_313_awake = abs(hilbert(eeg_313_awake));
eeg_amp_318_awake = abs(hilbert(eeg_318_awake));

eeg_amp_210_ket = abs(hilbert(eeg_210_ket));
eeg_amp_219_ket = abs(hilbert(eeg_219_ket));
eeg_amp_249_ket = abs(hilbert(eeg_249_ket));
eeg_amp_251_ket = abs(hilbert(eeg_251_ket));
eeg_amp_265_ket = abs(hilbert(eeg_265_ket));
eeg_amp_271_ket = abs(hilbert(eeg_271_ket));
eeg_amp_282_ket = abs(hilbert(eeg_282_ket));
eeg_amp_300_ket = abs(hilbert(eeg_300_ket));
eeg_amp_313_ket = abs(hilbert(eeg_313_ket));
eeg_amp_318_ket = abs(hilbert(eeg_318_ket));

% Binarize each channel signal using its mean as a threshold
binary_210_awake = eeg_amp_210_awake > mean(eeg_amp_210_awake,2);
binary_219_awake = eeg_amp_219_awake > mean(eeg_amp_219_awake,2);
binary_249_awake = eeg_amp_249_awake > mean(eeg_amp_249_awake,2);
binary_251_awake = eeg_amp_251_awake > mean(eeg_amp_251_awake,2);
binary_265_awake = eeg_amp_265_awake > mean(eeg_amp_265_awake,2);
binary_271_awake = eeg_amp_271_awake > mean(eeg_amp_271_awake,2);
binary_282_awake = eeg_amp_282_awake > mean(eeg_amp_282_awake,2);
binary_300_awake = eeg_amp_300_awake > mean(eeg_amp_300_awake,2);
binary_313_awake = eeg_amp_313_awake > mean(eeg_amp_313_awake,2);
binary_318_awake = eeg_amp_318_awake > mean(eeg_amp_318_awake,2);

binary_210_ket = eeg_amp_210_ket > mean(eeg_amp_210_ket,2);
binary_219_ket = eeg_amp_219_ket > mean(eeg_amp_219_ket,2);
binary_249_ket = eeg_amp_249_ket > mean(eeg_amp_249_ket,2);
binary_251_ket = eeg_amp_251_ket > mean(eeg_amp_251_ket,2);
binary_265_ket = eeg_amp_265_ket > mean(eeg_amp_265_ket,2);
binary_271_ket = eeg_amp_271_ket > mean(eeg_amp_271_ket,2);
binary_282_ket = eeg_amp_282_ket > mean(eeg_amp_282_ket,2);
binary_300_ket = eeg_amp_300_ket > mean(eeg_amp_300_ket,2);
binary_313_ket = eeg_amp_313_ket > mean(eeg_amp_313_ket,2);
binary_318_ket = eeg_amp_318_ket > mean(eeg_amp_318_ket,2);

% Calculate single-channel (temporal) Lempel-Ziv complexity (LZs) for each epoch using the LZW algorithm
for index1 = 1:size(binary_210_awake,1) % loop over channels

    for index2 = 1:(size(binary_210_awake,2)/n_samples) % loop over epochs
        LZs_210_awake(index1,index2) = lzwNormalised(binary_210_awake(index1,(index2-1)*n_samples+1:index2*n_samples),1);
    end

    for index2 = 1:(size(binary_219_awake,2)/n_samples) % loop over epochs
        LZs_219_awake(index1,index2) = lzwNormalised(binary_219_awake(index1,(index2-1)*n_samples+1:index2*n_samples),1);
    end

    for index2 = 1:(size(binary_249_awake,2)/n_samples) % loop over epochs
        LZs_249_awake(index1,index2) = lzwNormalised(binary_249_awake(index1,(index2-1)*n_samples+1:index2*n_samples),1);
    end

    for index2 = 1:(size(binary_251_awake,2)/n_samples) % loop over epochs
        LZs_251_awake(index1,index2) = lzwNormalised(binary_251_awake(index1,(index2-1)*n_samples+1:index2*n_samples),1);
    end

    for index2 = 1:(size(binary_265_awake,2)/n_samples) % loop over epochs
        LZs_265_awake(index1,index2) = lzwNormalised(binary_265_awake(index1,(index2-1)*n_samples+1:index2*n_samples),1);
    end

    for index2 = 1:(size(binary_271_awake,2)/n_samples) % loop over epochs
        LZs_271_awake(index1,index2) = lzwNormalised(binary_271_awake(index1,(index2-1)*n_samples+1:index2*n_samples),1);
    end

    for index2 = 1:(size(binary_282_awake,2)/n_samples) % loop over epochs
        LZs_282_awake(index1,index2) = lzwNormalised(binary_282_awake(index1,(index2-1)*n_samples+1:index2*n_samples),1);
    end

    for index2 = 1:(size(binary_300_awake,2)/n_samples) % loop over epochs
        LZs_300_awake(index1,index2) = lzwNormalised(binary_300_awake(index1,(index2-1)*n_samples+1:index2*n_samples),1);
    end

    for index2 = 1:(size(binary_313_awake,2)/n_samples) % loop over epochs
        LZs_313_awake(index1,index2) = lzwNormalised(binary_313_awake(index1,(index2-1)*n_samples+1:index2*n_samples),1);
    end

    for index2 = 1:(size(binary_318_awake,2)/n_samples) % loop over epochs
        LZs_318_awake(index1,index2) = lzwNormalised(binary_318_awake(index1,(index2-1)*n_samples+1:index2*n_samples),1);
    end

    for index2 = 1:(size(binary_210_ket,2)/n_samples) % loop over epochs
        LZs_210_ket(index1,index2) = lzwNormalised(binary_210_ket(index1,(index2-1)*n_samples+1:index2*n_samples),1);
    end

    for index2 = 1:(size(binary_219_ket,2)/n_samples) % loop over epochs
        LZs_219_ket(index1,index2) = lzwNormalised(binary_219_ket(index1,(index2-1)*n_samples+1:index2*n_samples),1);
    end

    for index2 = 1:(size(binary_249_ket,2)/n_samples) % loop over epochs
        LZs_249_ket(index1,index2) = lzwNormalised(binary_249_ket(index1,(index2-1)*n_samples+1:index2*n_samples),1);
    end

    for index2 = 1:(size(binary_251_ket,2)/n_samples) % loop over epochs
        LZs_251_ket(index1,index2) = lzwNormalised(binary_251_ket(index1,(index2-1)*n_samples+1:index2*n_samples),1);
    end

    for index2 = 1:(size(binary_265_ket,2)/n_samples) % loop over epochs
        LZs_265_ket(index1,index2) = lzwNormalised(binary_265_ket(index1,(index2-1)*n_samples+1:index2*n_samples),1);
    end

    for index2 = 1:(size(binary_271_ket,2)/n_samples) % loop over epochs
        LZs_271_ket(index1,index2) = lzwNormalised(binary_271_ket(index1,(index2-1)*n_samples+1:index2*n_samples),1);
    end

    for index2 = 1:(size(binary_282_ket,2)/n_samples) % loop over epochs
        LZs_282_ket(index1,index2) = lzwNormalised(binary_282_ket(index1,(index2-1)*n_samples+1:index2*n_samples),1);
    end

    for index2 = 1:(size(binary_300_ket,2)/n_samples) % loop over epochs
        LZs_300_ket(index1,index2) = lzwNormalised(binary_300_ket(index1,(index2-1)*n_samples+1:index2*n_samples),1);
    end

    for index2 = 1:(size(binary_313_ket,2)/n_samples) % loop over epochs
        LZs_313_ket(index1,index2) = lzwNormalised(binary_313_ket(index1,(index2-1)*n_samples+1:index2*n_samples),1);
    end

    for index2 = 1:(size(binary_318_ket,2)/n_samples) % loop over epochs
        LZs_318_ket(index1,index2) = lzwNormalised(binary_318_ket(index1,(index2-1)*n_samples+1:index2*n_samples),1);
    end

end

% For each condition, combine into a single matrix with all subjects
LZs_awake = [mean(LZs_210_awake,2)';
    mean(LZs_219_awake,2)';
    mean(LZs_249_awake,2)';
    mean(LZs_251_awake,2)';
    mean(LZs_265_awake,2)';
    mean(LZs_271_awake,2)';
    mean(LZs_282_awake,2)';
    mean(LZs_300_awake,2)';
    mean(LZs_313_awake,2)';
    mean(LZs_318_awake,2)'];

LZs_ket = [mean(LZs_210_ket,2)';
    mean(LZs_219_ket,2)';
    mean(LZs_249_ket,2)';
    mean(LZs_251_ket,2)';
    mean(LZs_265_ket,2)';
    mean(LZs_271_ket,2)';
    mean(LZs_282_ket,2)';
    mean(LZs_300_ket,2)';
    mean(LZs_313_ket,2)';
    mean(LZs_318_ket,2)'];

% Concatenate each binary matrix column-by-column into a single sequence
binary_seq_210_awake = reshape(binary_210_awake,[],1)';
binary_seq_219_awake = reshape(binary_219_awake,[],1)';
binary_seq_249_awake = reshape(binary_249_awake,[],1)';
binary_seq_251_awake = reshape(binary_251_awake,[],1)';
binary_seq_265_awake = reshape(binary_265_awake,[],1)';
binary_seq_271_awake = reshape(binary_271_awake,[],1)';
binary_seq_282_awake = reshape(binary_282_awake,[],1)';
binary_seq_300_awake = reshape(binary_300_awake,[],1)';
binary_seq_313_awake = reshape(binary_313_awake,[],1)';
binary_seq_318_awake = reshape(binary_318_awake,[],1)';

binary_seq_210_ket = reshape(binary_210_ket,[],1)';
binary_seq_219_ket = reshape(binary_219_ket,[],1)';
binary_seq_249_ket = reshape(binary_249_ket,[],1)';
binary_seq_251_ket = reshape(binary_251_ket,[],1)';
binary_seq_265_ket = reshape(binary_265_ket,[],1)';
binary_seq_271_ket = reshape(binary_271_ket,[],1)';
binary_seq_282_ket = reshape(binary_282_ket,[],1)';
binary_seq_300_ket = reshape(binary_300_ket,[],1)';
binary_seq_313_ket = reshape(binary_313_ket,[],1)';
binary_seq_318_ket = reshape(binary_318_ket,[],1)';

% Calculate spatiotemporal Lempel-Ziv complexity (LZc) for each epoch using the LZW algorithm
for index1 = 1:length(binary_seq_210_awake)/n_samples % loop over epochs
    LZc_210_awake(index1) = lzwNormalised(binary_seq_210_awake((index1-1)*n_samples+1:index1*n_samples),1);
end

for index1 = 1:length(binary_seq_219_awake)/n_samples % loop over epochs
    LZc_219_awake(index1) = lzwNormalised(binary_seq_219_awake((index1-1)*n_samples+1:index1*n_samples),1);
end

for index1 = 1:length(binary_seq_249_awake)/n_samples % loop over epochs
    LZc_249_awake(index1) = lzwNormalised(binary_seq_249_awake((index1-1)*n_samples+1:index1*n_samples),1);
end

for index1 = 1:length(binary_seq_251_awake)/n_samples % loop over epochs
    LZc_251_awake(index1) = lzwNormalised(binary_seq_251_awake((index1-1)*n_samples+1:index1*n_samples),1);
end

for index1 = 1:length(binary_seq_265_awake)/n_samples % loop over epochs
    LZc_265_awake(index1) = lzwNormalised(binary_seq_265_awake((index1-1)*n_samples+1:index1*n_samples),1);
end

for index1 = 1:length(binary_seq_271_awake)/n_samples % loop over epochs
    LZc_271_awake(index1) = lzwNormalised(binary_seq_271_awake((index1-1)*n_samples+1:index1*n_samples),1);
end

for index1 = 1:length(binary_seq_282_awake)/n_samples % loop over epochs
    LZc_282_awake(index1) = lzwNormalised(binary_seq_282_awake((index1-1)*n_samples+1:index1*n_samples),1);
end

for index1 = 1:length(binary_seq_300_awake)/n_samples % loop over epochs
    LZc_300_awake(index1) = lzwNormalised(binary_seq_300_awake((index1-1)*n_samples+1:index1*n_samples),1);
end

for index1 = 1:length(binary_seq_313_awake)/n_samples % loop over epochs
    LZc_313_awake(index1) = lzwNormalised(binary_seq_313_awake((index1-1)*n_samples+1:index1*n_samples),1);
end

for index1 = 1:length(binary_seq_318_awake)/n_samples % loop over epochs
    LZc_318_awake(index1) = lzwNormalised(binary_seq_318_awake((index1-1)*n_samples+1:index1*n_samples),1);
end

for index1 = 1:length(binary_seq_210_ket)/n_samples % loop over epochs
    LZc_210_ket(index1) = lzwNormalised(binary_seq_210_ket((index1-1)*n_samples+1:index1*n_samples),1);
end

for index1 = 1:length(binary_seq_219_ket)/n_samples % loop over epochs
    LZc_219_ket(index1) = lzwNormalised(binary_seq_219_ket((index1-1)*n_samples+1:index1*n_samples),1);
end

for index1 = 1:length(binary_seq_249_ket)/n_samples % loop over epochs
    LZc_249_ket(index1) = lzwNormalised(binary_seq_249_ket((index1-1)*n_samples+1:index1*n_samples),1);
end

for index1 = 1:length(binary_seq_251_ket)/n_samples % loop over epochs
    LZc_251_ket(index1) = lzwNormalised(binary_seq_251_ket((index1-1)*n_samples+1:index1*n_samples),1);
end

for index1 = 1:length(binary_seq_265_ket)/n_samples % loop over epochs
    LZc_265_ket(index1) = lzwNormalised(binary_seq_265_ket((index1-1)*n_samples+1:index1*n_samples),1);
end

for index1 = 1:length(binary_seq_271_ket)/n_samples % loop over epochs
    LZc_271_ket(index1) = lzwNormalised(binary_seq_271_ket((index1-1)*n_samples+1:index1*n_samples),1);
end

for index1 = 1:length(binary_seq_282_ket)/n_samples % loop over epochs
    LZc_282_ket(index1) = lzwNormalised(binary_seq_282_ket((index1-1)*n_samples+1:index1*n_samples),1);
end

for index1 = 1:length(binary_seq_300_ket)/n_samples % loop over epochs
    LZc_300_ket(index1) = lzwNormalised(binary_seq_300_ket((index1-1)*n_samples+1:index1*n_samples),1);
end

for index1 = 1:length(binary_seq_313_ket)/n_samples % loop over epochs
    LZc_313_ket(index1) = lzwNormalised(binary_seq_313_ket((index1-1)*n_samples+1:index1*n_samples),1);
end

for index1 = 1:length(binary_seq_318_ket)/n_samples % loop over epochs
    LZc_318_ket(index1) = lzwNormalised(binary_seq_318_ket((index1-1)*n_samples+1:index1*n_samples),1);
end

% For each condition, combine into a single matrix with all subjects
LZc_awake = [mean(LZc_210_awake);
    mean(LZc_219_awake);
    mean(LZc_249_awake);
    mean(LZc_251_awake);
    mean(LZc_265_awake);
    mean(LZc_271_awake);
    mean(LZc_282_awake);
    mean(LZc_300_awake);
    mean(LZc_313_awake);
    mean(LZc_318_awake)];

LZc_ket = [mean(LZc_210_ket);
    mean(LZc_219_ket);
    mean(LZc_249_ket);
    mean(LZc_251_ket);
    mean(LZc_265_ket);
    mean(LZc_271_ket);
    mean(LZc_282_ket);
    mean(LZc_300_ket);
    mean(LZc_313_ket);
    mean(LZc_318_ket)];

%% Perform statistical analyses

% Compute effect sizes (Cohen's d)
effect_size_LZs_P6 = meanEffectSize(LZs_awake(:,1),LZs_ket(:,1),Paired=true,Effect="cohen",Alpha=0.05);
effect_size_LZs_Pz = meanEffectSize(LZs_awake(:,2),LZs_ket(:,2),Paired=true,Effect="cohen",Alpha=0.05);
effect_size_LZs_P5 = meanEffectSize(LZs_awake(:,3),LZs_ket(:,3),Paired=true,Effect="cohen",Alpha=0.05);
effect_size_LZs_C6 = meanEffectSize(LZs_awake(:,4),LZs_ket(:,4),Paired=true,Effect="cohen",Alpha=0.05);
effect_size_LZs_Cz = meanEffectSize(LZs_awake(:,5),LZs_ket(:,5),Paired=true,Effect="cohen",Alpha=0.05);
effect_size_LZs_C5 = meanEffectSize(LZs_awake(:,6),LZs_ket(:,6),Paired=true,Effect="cohen",Alpha=0.05);
effect_size_LZs_F6 = meanEffectSize(LZs_awake(:,7),LZs_ket(:,7),Paired=true,Effect="cohen",Alpha=0.05);
effect_size_LZs_Fz = meanEffectSize(LZs_awake(:,8),LZs_ket(:,8),Paired=true,Effect="cohen",Alpha=0.05);
effect_size_LZs_F5 = meanEffectSize(LZs_awake(:,9),LZs_ket(:,9),Paired=true,Effect="cohen",Alpha=0.05);
effect_size_LZs_all = double([effect_size_LZs_P6{:,1},effect_size_LZs_Pz{:,1},effect_size_LZs_P5{:,1},effect_size_LZs_C6{:,1},effect_size_LZs_Cz{:,1},effect_size_LZs_C5{:,1},effect_size_LZs_F6{:,1},effect_size_LZs_Fz{:,1},effect_size_LZs_F5{:,1}]);
effect_size_LZs = meanEffectSize(mean(LZs_awake,2),mean(LZs_ket,2),Paired=true,Effect="cohen",Alpha=0.05);
effect_size_LZc = meanEffectSize(LZc_awake,LZc_ket,Paired=true,Effect="cohen",Alpha=0.05);

%% Export data

writematrix([mean(LZs_awake,2), LZc_awake], 'complexity_awake.csv');
writematrix([mean(LZs_ket,2), LZc_ket], 'complexity_ket.csv');

writematrix([effect_size_LZs_F5{:,"Effect"}, effect_size_LZs_F5{:,"ConfidenceIntervals"}(:,1), effect_size_LZs_F5{:,"ConfidenceIntervals"}(:,2);
    effect_size_LZs_Fz{:,"Effect"}, effect_size_LZs_Fz{:,"ConfidenceIntervals"}(:,1), effect_size_LZs_Fz{:,"ConfidenceIntervals"}(:,2);
    effect_size_LZs_F6{:,"Effect"}, effect_size_LZs_F6{:,"ConfidenceIntervals"}(:,1), effect_size_LZs_F6{:,"ConfidenceIntervals"}(:,2);
    effect_size_LZs_C5{:,"Effect"}, effect_size_LZs_C5{:,"ConfidenceIntervals"}(:,1), effect_size_LZs_C5{:,"ConfidenceIntervals"}(:,2);
    effect_size_LZs_Cz{:,"Effect"}, effect_size_LZs_Cz{:,"ConfidenceIntervals"}(:,1), effect_size_LZs_Cz{:,"ConfidenceIntervals"}(:,2);
    effect_size_LZs_C6{:,"Effect"}, effect_size_LZs_C6{:,"ConfidenceIntervals"}(:,1), effect_size_LZs_C6{:,"ConfidenceIntervals"}(:,2);
    effect_size_LZs_P5{:,"Effect"}, effect_size_LZs_P5{:,"ConfidenceIntervals"}(:,1), effect_size_LZs_P5{:,"ConfidenceIntervals"}(:,2);
    effect_size_LZs_Pz{:,"Effect"}, effect_size_LZs_Pz{:,"ConfidenceIntervals"}(:,1), effect_size_LZs_Pz{:,"ConfidenceIntervals"}(:,2);
    effect_size_LZs_P6{:,"Effect"}, effect_size_LZs_P6{:,"ConfidenceIntervals"}(:,1), effect_size_LZs_P6{:,"ConfidenceIntervals"}(:,2);
    effect_size_LZs{:,"Effect"}, effect_size_LZs{:,"ConfidenceIntervals"}(:,1), effect_size_LZs{:,"ConfidenceIntervals"}(:,2);
    effect_size_LZc{:,"Effect"}, effect_size_LZc{:,"ConfidenceIntervals"}(:,1), effect_size_LZc{:,"ConfidenceIntervals"}(:,2)], 'effect_size_complexity.csv');