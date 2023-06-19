% Energy Sources in Smart Homes...

sources(grid).
sources(solar).
sources(generator).

% energy Storage for emergency...

energy_storage(battery).



% Types of the weather conditions...

%weather(sunny).
%weather(cloudy).
%weather(rainy).
%weather(windy).
%weather(stormy).
%weather(foggy).

% Energy Consumed Materials...

consumed(heating_system).
consumed(cooling_system).
consumed(appliances).
consumed(entertainment_system).
consumed(office_equipment).
consumed(lighting).

%Grid Electrycity status...
%grid_status(on).
%grid_status(off).

%time(day).
%time(night).

solar_status(on) :- weather(sunny),time(day).
solar_status(off) :- weather(sunny),time(night).
solar_status(off) :- weather(cloudy).
solar_status(off) :- weather(rainy).
solar_status(off) :- weather(windy).
solar_status(off) :- weather(stormy).
solar_status(off) :- weather(foggy).

% Battery Status...
battery_status(use) :- grid_status(off).
battery_status(charge):- solar_status(on);grid_status(on).
battery_status(empty):- solar_status(off),grid_status(off),weather(rainy).

%Generator Status rule
generator_status(on):- grid_status(off),battery_status(empty).
generator_status(off):- grid_status(on);battery_status(use).

%Rules for the energy sources switching for power...
use_source(grid) :- grid_status(on).
use_source(battery) :- grid_status(off).
use_source(generator) :- grid_status(off),battery_status(empty).


temperature(35):- weather(sunny).
temperature(20):- weather(cloudy).
temperature(18):- weather(rainy).
temperature(19):- weather(windy).
temperature(20):- weather(stormy).
temperature(9):- weather(foggy).

%Rule for the smart thermostat system
raise_temp(20):- temperature(35).
raise_temp(25):- temperature(20).
raise_temp(23):- temperature(18).
raise_temp(23):- temperature(19).
raise_temp(26):- temperature(9).


%occupancy(yes).
%occupancy(no).

%Rule for the lighteing
lights(off):- occupancy(no).
lights(on):- occupancy(yes).

%monitor(use).
%monitor(not_use).

appliance(use):- monitor(use).
appliance(off):- monitor(not_use).

entertainment_system(off):- people(no).
entertainment_system(on):- people(yes).



%% Energy-efficient appliances in Smart Homes...
%
%% Define energy-efficient appliances...
%energy_efficient(led_bulb).
%energy_efficient(smart_thermostat).
%
%% Define energy consumption of appliances...
%consumption(heating_system, 1000).
%consumption(cooling_system, 1500).
%consumption(appliances, 500).
%consumption(entertainment_system, 800).
%consumption(office_equipment, 600).
%consumption(lighting, 200).
%
%% Rule for using energy-efficient appliances...
%use_energy_efficient_appliances :-
%    energy_efficient(Appliance),
%    consumption(Appliance, Consumption),
%    Consumption < 500.
%
%% Rule for turning off appliances when not in use...
%turn_off_appliances :-
%    consumption(Appliance, Consumption),
%    Consumption > 0,
%    \+ in_use(Appliance).
%
%% Rule for checking if an appliance is in use...
%in_use(Appliance) :-
%    current_activity(Activity),
%    uses(Activity, Appliance).
%
%% Define activities that use appliances...
%uses(watching_tv, entertainment_system).
%uses(working, office_equipment).
%uses(cooking, appliances).
%uses(lighting_room, lighting).
%
%% Define current activity...
%current_activity(watching_tv).
%
%% Rules for energy-efficient home design...
%
%insulation(proper).
%windows(double_pane).
%doors(energy_efficient).
%
%% A home is considered energy-efficient if it has proper insulation,
%% double-pane windows, and energy-efficient doors...
%
%is_energy_efficient(Home) :-
%    insulation(proper),
%    windows(double_pane),
%    doors(energy_efficient),
%    Home = energy_efficient_home.
%
%% Rules for energy consumption based on occupancy
%
%% Occupancy can be high or low
%occupancy(high).
%occupancy(low).
%
%% Rules for energy consumption based on occupancy
%consume_energy(lights, high) :-
%    room_status(empty).
%
%consume_energy(appliances, high) :-
%    room_status(empty).
%
%consume_energy(lights, low) :-
%    room_status(occupied).
%
%consume_energy(appliances, low) :-
%    room_status(occupied).
%
%% A room is considered empty if it has no occupants...
%room_status(empty) :-
%    occupants(0).
%
%% A room is considered occupied if it has one or more occupants...
%room_status(occupied) :-
%    occupants(Occupants), Occupants > 0.



