# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_count_harvest_recursive.py                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ripaparo <ripaparo@student.42madrid.fr>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/11/28 18:25:37 by ripaparo          #+#    #+#              #
#    Updated: 2025/11/28 18:55:27 by ripaparo         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def	ft_count_harvest_recursive():
	days = int(input("Days until harvest: "));

	def	print_days(n):
		if days > n