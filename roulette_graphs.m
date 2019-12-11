clear

evenlist = [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36]; %numbers contained in the even bin (equal to prob of black, red, etc.)
highest_balance = 0;
top_balance_roll = [];
roll_matrix = zeros(2,2);
balance_matrix = zeros(2,2);

prompt ='\nHow many simulations will you run? ';
num_simulation = input(prompt);
if rem(num_simulation, 2) ~= 0 %in order to get a median later, the #of sims must always be odd
    num_simulation = num_simulation+1;
end

prompt2 ='\nWhat is your starting balance? ';
hard_balance = input(prompt2);

for i = 0:num_simulation %generate many vectors
    roll_at_highest_balance = 0;
    highest_balance = 0;
    current_roll = 0;
    balance = hard_balance;
    bet = 5;
    resetbet = bet;
    
    balance_vector = [];
    rolls = [];
    
    while balance > 0
        if (balance - bet) >= 0
            balance = balance - bet;
            
            landon = randi([0 36],1,1);
            
            if ismember(landon,evenlist)
                balance = balance + bet*2;
                bet = resetbet;
            else
                bet = bet*2;
            end
            
        else
            balance = 0; %balance negative therefore gameover
        end
        balance_vector = [balance_vector, balance];
        current_roll   = current_roll+1; %increment roll count
        rolls          = [rolls, current_roll]; %create x vector for the number of rolls
        
        %end of roll checks
        if balance > highest_balance
            highest_balance = balance; %find highest balance
            roll_at_highest_balance = current_roll;
        end
    end
    
    roll_matrix(i+1,1:length(rolls)) = rolls; %fill matrix with rows of multiple games
    balance_matrix(i+1,1:length(balance_vector)) = balance_vector;
    
    top_balance_roll = [top_balance_roll, roll_at_highest_balance]; %find at which roll the max balance was obtained
end

discard_highest_balance = max(top_balance_roll);
%top_balance_roll(top_balance_roll==discard_highest_balance) = []; %found the highest balance and discard it for safety

% to figure where the optimal stopping point, find the median
index_of_median = find(top_balance_roll == median(top_balance_roll),1); %search for the first element that is greater than or equal to the median
median_rolls_for_max_balance = top_balance_roll(index_of_median); %find the roll optimal stopping value at the median

%get the vectors of the optimal stopping game in the matrices
V = roll_matrix(index_of_median,:); %get row vector at the proper simulation number Xaxis
V(:,~any(V,1)) = [];
limit = V(end);
W = balance_matrix(index_of_median,1:limit); %get the equivalent address in the balance matrix Yaxis

%plot the vector at the median roll
figure(1)
title('The most likely roulette scenario to occur')
plot(V,W,'-o')
grid on
xlabel('Rolls')
ylabel('Balance')
xlim([0 max(V)+2])
ylim([0 max(W)]+10)
ytickformat('usd')
xline(median_rolls_for_max_balance)

fprintf('\n%.0f simulations predict that you should cash-out before %.0f rolls.\n',num_simulation,median_rolls_for_max_balance);


