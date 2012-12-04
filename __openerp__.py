# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) Javier Duran
#                  Mariano Ruiz (Enterprise Objects Consulting)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
	"name" : "Purchase extension to search or filter by supplier the products in the purchase order lines",
	"version" : "0.1",
	"author" : "Javier Duran, Enterprise Objects Consulting",
	"depends" : ["product", "purchase"],
	"description": """Allow to limit available selection of Products in a Purchase Order only to those products that are supplied by selected supplier,
	and find them by supplier product name or supplier product code.""",
	"website" : "http://www.eoconsulting.com.ar",
	"category" : "Purchase Management",
	"init_xml" : [],
	"demo_xml" : [],
	"update_xml" : ["purchase_supplier_view.xml"],
	"active": False,
	"installable": True
}
