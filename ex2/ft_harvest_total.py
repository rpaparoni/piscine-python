# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_harvest_total.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ripaparo <ripaparo@student.42madrid.fr>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/11/28 16:47:40 by ripaparo          #+#    #+#              #
#    Updated: 2025/11/28 16:59:19 by ripaparo         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_harvest_total():
	a = input("Day 1 harvest: ");
	b = input("Day 2 harvest: ");
	c = input("Day 3 harvest: ");

	total = int(a) + int(b) + int(c);

	print("Total harvest: ", total);