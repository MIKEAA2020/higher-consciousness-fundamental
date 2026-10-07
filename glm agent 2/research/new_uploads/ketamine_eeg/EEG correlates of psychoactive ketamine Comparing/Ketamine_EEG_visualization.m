%% EEG Correlates of Psychoactive Ketamine: Spectral Power and Complexity
% Author: Brandon Reynante
% Revision Date: 2026-02-22
% This code visualizes the spectral power and complexity results

clear; clc; close all;

%% Load data

% Whole-brain EEG spectral power and complexity values
power_awake = readmatrix('../Data/power_awake.csv');
power_ket = readmatrix('../Data/power_ket.csv');
complexity_awake = readmatrix('../Data/complexity_awake.csv');
complexity_ket = readmatrix('../Data/complexity_ket.csv');

% Effect size data (whole-brain and source-localized)
effect_size_delta = readmatrix('../Data/effect_size_delta.csv');
effect_size_theta = readmatrix('../Data/effect_size_theta.csv');
effect_size_alpha = readmatrix('../Data/effect_size_alpha.csv');
effect_size_beta = readmatrix('../Data/effect_size_beta.csv');
effect_size_gamma = readmatrix('../Data/effect_size_gamma.csv');
effect_size_complexity = readmatrix('../Data/effect_size_complexity.csv');

% Phenomenology and correlation data
ASC = readmatrix('../Data/11D-ASC.csv');
ASC = [ASC; mean(ASC,1)]';
Rho = readmatrix('../Data/rho.csv');
rho_strong = readmatrix('../Data/rho_strong.csv');

%% Create estimation plots

% Spectral power
figure
estimation_plot_power = tiledlayout(3, 1);

nexttile([2, 1])
hold on
plot([2*ones(1,10); 5*ones(1,10)],[power_awake(:,1)'; power_ket(:,1)'],"-o",'Color',[.7 .7 .7])
errorbar(1.5, mean(power_awake(:,1)), std(power_awake(:,1))/sqrt(length(power_awake(:,1))),"ok") % SEM
errorbar(5.5, mean(power_ket(:,1)), std(power_ket(:,1))/sqrt(length(power_ket(:,1))),"ok") % SEM
plot([8*ones(1,10); 11*ones(1,10)],[power_awake(:,2)'; power_ket(:,2)'],"-o",'Color',[.7 .7 .7])
errorbar(7.5, mean(power_awake(:,2)), std(power_awake(:,2))/sqrt(length(power_awake(:,2))),"ok") % SEM
errorbar(11.5, mean(power_ket(:,2)), std(power_ket(:,2))/sqrt(length(power_ket(:,2))),"ok") % SEM
plot([14*ones(1,10); 17*ones(1,10)],[power_awake(:,3)'; power_ket(:,3)'],"-o",'Color',[.7 .7 .7])
errorbar(13.5, mean(power_awake(:,3)), std(power_awake(:,3))/sqrt(length(power_awake(:,3))),"ok") % SEM
errorbar(17.5, mean(power_ket(:,3)), std(power_ket(:,3))/sqrt(length(power_ket(:,3))),"ok") % SEM
plot([20*ones(1,10); 23*ones(1,10)],[power_awake(:,4)'; power_ket(:,4)'],"-o",'Color',[.7 .7 .7])
errorbar(19.5, mean(power_awake(:,4)), std(power_awake(:,4))/sqrt(length(power_awake(:,4))),"ok") % SEM
errorbar(23.5, mean(power_ket(:,4)), std(power_ket(:,4))/sqrt(length(power_ket(:,4))),"ok") % SEM
plot([26*ones(1,10); 29*ones(1,10)],[power_awake(:,5)'; power_ket(:,5)'],"-o",'Color',[.7 .7 .7])
errorbar(25.5, mean(power_awake(:,5)), std(power_awake(:,5))/sqrt(length(power_awake(:,5))),"ok") % SEM
errorbar(29.5, mean(power_ket(:,5)), std(power_ket(:,5))/sqrt(length(power_ket(:,5))),"ok") % SEM
xlim([0 31])
box on
axis on; ax = gca; ax.FontSize = 12; ax.XAxis.TickLength = [0 0];
xtickangle(0);
xticks([2 3.5 5 8 9.5 11 14 15.5 17 20 21.5 23 26 27.5 29])
xticklabels({'Awake' sprintf('\\newlineDelta') 'Ketamine' 'Awake' sprintf('\\newlineTheta') 'Ketamine' 'Awake' sprintf('\\newlineAlpha') 'Ketamine' 'Awake' sprintf('\\newlineBeta') 'Ketamine' 'Awake' sprintf('\\newlineGamma') 'Ketamine'})
ylabel('Spectral Power (\muV^2)')

nexttile
hold on
errorbar(5, effect_size_delta(10,1), effect_size_delta(10,1) - effect_size_delta(10,2), effect_size_delta(10,3) - effect_size_delta(10,1), "squarek");
errorbar(11, effect_size_theta(10,1), effect_size_theta(10,1) - effect_size_theta(10,2), effect_size_theta(10,3) - effect_size_theta(10,1), "squarek");
errorbar(17, effect_size_alpha(10,1), effect_size_alpha(10,1) - effect_size_alpha(10,2), effect_size_alpha(10,3) - effect_size_alpha(10,1), "squarek");
errorbar(23, effect_size_beta(10,1), effect_size_beta(10,1) - effect_size_beta(10,2), effect_size_beta(10,3) - effect_size_beta(10,1), "squarek");
errorbar(29, effect_size_gamma(10,1), effect_size_gamma(10,1) - effect_size_gamma(10,2), effect_size_gamma(10,3) - effect_size_gamma(10,1), "squarek");
yline(0);
xlim([0 31])
ylim([-1 3])
box on
axis on; ax = gca; ax.FontSize = 12; ax.XAxis.TickLength = [0 0];
xticks([5 11 17 23 29])
xticklabels({'Delta' 'Theta' 'Alpha' 'Beta' 'Gamma'});
ylabel("Cohen's d")

% Complexity
figure
estimation_plot_LZ = tiledlayout(1,2);

nexttile
hold on
gardnerAltmanPlot(complexity_awake(:,1),complexity_ket(:,1),Paired=true,Effect="cohen",Alpha=0.05);
errorbar(1, mean(complexity_awake(:,1)), std(complexity_awake(:,1))/sqrt(10), "o") % standard error of the mean
errorbar(2, mean(complexity_ket(:,1)), std(complexity_ket(:,1))/sqrt(10), "o") % standard error of the mean
line = findobj(gca,'Type','line'); set(line,'Marker','o','Color',[.7 .7 .7]);
CI = findobj(gca,'Type','errorbar'); set(CI,'Color','black');
plot([1; 3], [mean(complexity_awake(:,1)); mean(complexity_awake(:,1))],"--",'Color',[0 0 0])
plot([2; 3], [mean(complexity_ket(:,1)); mean(complexity_ket(:,1))],"--",'Color',[0 0 0])
ax = gca; ax.FontSize = 12; ax.YAxis(2).Color = [0 0 0]; set(gca,'Box','on'); ytickformat(ax, '%.2f');
title('Temporal Complexity (LZs)')
ylabel('Lempel-Ziv Complexity')
xticklabels({'Awake','Ketamine',"Cohen's d"})

nexttile
hold on
gardnerAltmanPlot(complexity_awake(:,2),complexity_ket(:,2),Paired=true,Effect="cohen",Alpha=0.05);
errorbar(1, mean(complexity_awake(:,2)), std(complexity_awake(:,2))/sqrt(10), "o") % standard error of the mean
errorbar(2, mean(complexity_ket(:,2)), std(complexity_ket(:,2))/sqrt(10), "o") % standard error of the mean
line = findobj(gca,'Type','line'); set(line,'Marker','o','Color',[.7 .7 .7]);
CI = findobj(gca,'Type','errorbar'); set(CI,'Color','black');
plot([1; 3], [mean(complexity_awake(:,2)); mean(complexity_awake(:,2))],"--",'Color',[0 0 0])
plot([2; 3], [mean(complexity_ket(:,2)); mean(complexity_ket(:,2))],"--",'Color',[0 0 0])
ax = gca; ax.FontSize = 12; ax.YAxis(2).Color = [0 0 0]; set(gca,'Box','on'); ytickformat(ax, '%.2f');
title('Spatiotemporal Complexity (LZc)')
ylabel('Lempel-Ziv Complexity')
xticklabels({'Awake','Ketamine',"Cohen's d"})

%% Create scalp topography plots

ch_list = {'F5','Fz','F6','C5','Cz','C6','P5','Pz','P6'};

figure
scalp_plot = tiledlayout(2,3);

ax1 = nexttile;
plot_topography(ch_list, effect_size_delta(1:9,1));
colorbar('off')
title("Delta Power");

ax2 = nexttile;
plot_topography(ch_list, effect_size_theta(1:9,1));
colorbar('off')
title("Theta Power");

ax3 = nexttile;
plot_topography(ch_list, effect_size_alpha(1:9,1));
colorbar('off')
title("Alpha Power");

ax4 = nexttile;
plot_topography(ch_list, effect_size_beta(1:9,1));
colorbar('off')
title("Beta Power");

ax5 = nexttile;
plot_topography(ch_list, effect_size_gamma(1:9,1));
colorbar('off')
title("Gamma Power");

ax6 = nexttile;
plot_topography(ch_list, effect_size_complexity(1:9,1));
colorbar('off')
title("Temporal Complexity");

linkprop([ax1 ax2 ax3 ax4 ax5 ax6], 'Clim');
colormap(turbo); clim([-1.5 1.5]);
cb = colorbar; cb.Layout.Tile = 'west'; cb.FontSize = 12;
ylabel(cb,"Cohen's d",'FontSize',12)

%% Create channel effect size plots

figure
channel_effect_size_plot = tiledlayout(2,3);

nexttile
hold on
errorbar(1:9,effect_size_delta(1:9,1),(effect_size_delta(1:9,2) - effect_size_delta(1:9,1)),(effect_size_delta(1:9,1) - effect_size_delta(1:9,3)),"squarek",'LineStyle', 'none')
yline(0,'-')
box on
xlim([0 10])
ylim([-2 3])
xticks(1:9); xtickangle(45);
xticklabels({'F5','Fz','F6','C5','Cz','C6','P5','Pz','P6'})
xlabel('Channel Locations')
ylabel("Cohen's d")
title('Delta Power')

nexttile
hold on
errorbar(1:9,effect_size_theta(1:9,1),(effect_size_theta(1:9,2) - effect_size_theta(1:9,1)),(effect_size_theta(1:9,1) - effect_size_theta(1:9,3)),"squarek",'LineStyle', 'none')
yline(0,'-')
box on
xlim([0 10])
ylim([-2 3])
xticks(1:9); xtickangle(45);
xticklabels({'F5','Fz','F6','C5','Cz','C6','P5','Pz','P6'})
xlabel('Channel Locations')
ylabel("Cohen's d")
title('Theta Power')

nexttile
hold on
errorbar(1:9,effect_size_alpha(1:9,1),(effect_size_alpha(1:9,2) - effect_size_alpha(1:9,1)),(effect_size_alpha(1:9,1) - effect_size_alpha(1:9,3)),"squarek",'LineStyle', 'none')
yline(0,'-')
box on
xlim([0 10])
ylim([-2 3])
xticks(1:9); xtickangle(45);
xticklabels({'F5','Fz','F6','C5','Cz','C6','P5','Pz','P6'})
xlabel('Channel Locations')
ylabel("Cohen's d")
title('Alpha Power')

nexttile
hold on
errorbar(1:9,effect_size_beta(1:9,1),(effect_size_beta(1:9,2) - effect_size_beta(1:9,1)),(effect_size_beta(1:9,1) - effect_size_beta(1:9,3)),"squarek",'LineStyle', 'none')
yline(0,'-')
box on
xlim([0 10])
ylim([-2 3])
xticks(1:9); xtickangle(45);
xticklabels({'F5','Fz','F6','C5','Cz','C6','P5','Pz','P6'})
xlabel('Channel Locations')
ylabel("Cohen's d")
title('Beta Power')

nexttile
hold on
errorbar(1:9,effect_size_gamma(1:9,1),(effect_size_gamma(1:9,2) - effect_size_gamma(1:9,1)),(effect_size_gamma(1:9,1) - effect_size_gamma(1:9,3)),"squarek",'LineStyle', 'none')
yline(0,'-')
box on
xlim([0 10])
ylim([-2 3])
xticks(1:9); xtickangle(45);
xticklabels({'F5','Fz','F6','C5','Cz','C6','P5','Pz','P6'})
xlabel('Channel Locations')
ylabel("Cohen's d")
title('Gamma Power')

nexttile
hold on
errorbar(1:9,effect_size_complexity(1:9,1),(effect_size_complexity(1:9,2) - effect_size_complexity(1:9,1)),(effect_size_complexity(1:9,1) - effect_size_complexity(1:9,3)),"squarek",'LineStyle', 'none')
yline(0,'-')
box on
xlim([0 10])
ylim([-2 3])
xticks(1:9); xtickangle(45);
xticklabels({'F5','Fz','F6','C5','Cz','C6','P5','Pz','P6'})
xlabel('Channel Locations')
ylabel("Cohen's d")
title('Temporal Complexity')

%% Plot phenomenology and correlations

figure
phenomenology_correlations_plot = tiledlayout(2,2);

% ASC data
nexttile([1,2])
bar(ASC(:,1:11))
axis on; ax = gca; ax.XAxis.TickLength = [0 0]; ax.YAxis.TickLength = [0 0];
ax.YAxisLocation = 'right';
colororder("gem12")
xlabel('Participants')
title('11D-ASC Scores')
legend('Experience of Unity','Spiritual Experience','Blissful State', ...
    'Insightfulness','Disembodiment','Impaired Control', ...
    'Anxiety','Complex Imagery','Elementary Imagery', ...
    'Synesthesia','Changed Percepts','Location','westoutside')

% Correlations
nexttile
rho_cutoff = 0.5;
imagesc(Rho');
newmap = turbo; % define custom color map based on existing map (turbo)
c = colorbar; clim([-1 1]);
nrow = size(newmap,1);
zpos1 = 1 + floor((0.5 - rho_cutoff/2) * nrow);
zpos2 = 1 + floor((0.5 + rho_cutoff/2) * nrow);
newmap(zpos1:zpos2,:) = ones(length(newmap(zpos1:zpos2)),3); % set center of colorbar interval to white
colormap(newmap);
c.Label.String = 'Pearson Correlation Coefficient'; c.Label.Rotation = 270;
axis on; ax = gca; ax.XAxis.TickLength = [0 0]; ax.YAxis.TickLength = [0 0];
yticks(1:12);
yticklabels({'Experience of Unity','Spiritual Experience','Blissful State','Insightfulness', ...
    'Disembodiment','Impaired Control','Anxiety','Complex Imagery', ...
    'Elementary Imagery','Synesthesia','Changed Percepts','Global ASC'})
xticks(1:7);
xticklabels({'Delta','Theta','Alpha','Beta','Gamma','LZs','LZc'})

% Correlation confidence intervals
nexttile
hold on
errorbar(flip(rho_strong(:,1)),1:length(rho_strong(:,1)),0,0,(flip(rho_strong(:,2)) - flip(rho_strong(:,1))),(flip(rho_strong(:,3)) - flip(rho_strong(:,1))),"squarek")
xline(0,'-')
box on
axis on; 
xlim([-1 1])
ylim([0 9])
xlabel('Pearson Correlation Coefficient')
yticks(1:8);
yticklabels({'Insightful x LZc','Insightful x Gamma','Blissful x Gamma','Blissful x Theta', ...
    'Spiritual x LZc','Spiritual x Gamma','Unity x LZc','Unity x Gamma'})

%% Export graphics

exportgraphics(estimation_plot_power,'EstimationPlotSpectralPower.pdf','ContentType','vector')
exportgraphics(estimation_plot_power,'EstimationPlotSpectralPower.png')

exportgraphics(estimation_plot_LZ,'EstimationPlotComplexity.pdf','ContentType','vector')
exportgraphics(estimation_plot_LZ,'EstimationPlotComplexity.png')

exportgraphics(scalp_plot,'ScalpPlot.jpg','Resolution','1000')
exportgraphics(scalp_plot,'ScalpPlot.png')

exportgraphics(channel_effect_size_plot,'ChannelEffectSizePlot.pdf','ContentType','vector')
exportgraphics(channel_effect_size_plot,'ChannelEffectSizePlot.png')

exportgraphics(phenomenology_correlations_plot,'PhenomenologyCorrelationsPlot.pdf','ContentType','vector')
exportgraphics(phenomenology_correlations_plot,'PhenomenologyCorrelationsPlot.png')