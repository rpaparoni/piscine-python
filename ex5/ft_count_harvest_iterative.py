# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_count_harvest_iterative.py                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ripaparo <ripaparo@student.42madrid.fr>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/11/28 17:51:32 by ripaparo          #+#    #+#              #
#    Updated: 2025/11/28 18:29:30 by ripaparo         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_count_harvest_iterative():
	days = input("Days until harvest: ")

	days = int(days);
	
	for i in range(1, days + 1):
		print("Day", i);
	print("Harvest time!");
