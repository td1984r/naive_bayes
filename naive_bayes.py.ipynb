{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "from flask import Flask, render_template, request"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Deo za povezivanje sa show.html dokumentom"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "\"\"\"\n",
    "app = Flask(__name__, static_folder='www')\n",
    "@app.route('/<path:path>')\n",
    "def static_file(path):\n",
    "    try:\n",
    "        return app.send_static_file(path)\n",
    "    except:\n",
    "        return \"Error\"\n",
    "\t\t\n",
    "@app.route('/')\n",
    "def root():\n",
    "    return app.send_static_file('show.html')\t\t\n",
    "\"\"\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "data = pd.DataFrame()\n",
    "\n",
    "import csv\n",
    "    \n",
    "linije = ''\n",
    "in_data = []\n",
    "with open('accepted_rejected_100K records.csv') as csvfile:\n",
    "    linije = csvfile.readlines()\n",
    "    \n",
    "for i, linija in enumerate(linije):\n",
    "    if i>0:\n",
    "        linija = linija.strip('\\n')\n",
    "        parts = linija.split(';')\n",
    "        in_data.append([parts[0], float(parts[1]), float(parts[2].replace('.', '')), float(parts[3])])\n",
    "    \n",
    "print(in_data)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "data = {}\n",
    "data['status'] = []"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "data['loan_amnt'] = []\n",
    "data['annual_inc'] = []\n",
    "data['emp_length_years'] = []\n",
    "\n",
    "# Create our target variable\n",
    "for el in in_data:\n",
    "    data['status'].append(el[0])\n",
    "    data['loan_amnt'].append(el[1])\n",
    "    data['annual_inc'].append(el[2])\n",
    "    data['emp_length_years'].append(el[3])    \n",
    "\n",
    "# View the data\n",
    "\n",
    "# Create an empty dataframe\n",
    "person = pd.DataFrame()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Deo koda koji bi trebao da poveze formu iz show.html dokumenta i preuzme vrednosti za input u okviru python file-a"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "\"\"\"\n",
    "app.run(host='0.0.0.0', port=8080, debug=True, use_reloader=True)\n",
    "\n",
    "loan_amnt = 0\n",
    "annual_inc = 0\n",
    "emp_length_years = 0\n",
    "\n",
    "@app.route('/send', methods=['GET', 'POST'])\n",
    "def send():\n",
    "\t\tif request.methods == 'POST':\n",
    "\t\t\tloan_amnt = request.form['loan_amnt']\n",
    "\t\t\tannual_inc = request.form['annual_inc']\n",
    "\t\t\temp_length_years = request.form['emp_length_years']\n",
    "\t\t\treturn loan_amnt\n",
    "\t\t\treturn annual_inc\n",
    "\t\t\treturn emp_length_years\n",
    "if __name__==\"__name__\":\n",
    "\tapp.run()\n",
    "\n",
    "# Create some feature values for this single row\n",
    "person['loan_amnt'] = loan_amnt.append\n",
    "person['annual_inc'] = annual_inc.append\n",
    "person['emp_length_years'] = emp_length_years\n",
    "\n",
    "print(person['loan_amnt'])\n",
    "\"\"\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "person['loan_amnt'] = [5000]\n",
    "person['annual_inc'] = [50000]\n",
    "person['emp_length_years'] = [5]\n",
    "\n",
    "# View the data \n",
    "person\n",
    "\n",
    "outdata_full = pd.DataFrame(data, columns=['status', 'loan_amnt', 'annual_inc', 'emp_length_years'])\n",
    "\n",
    "outdata_status = pd.DataFrame(data['status'], columns=['status'])\n",
    "\n",
    "# Number of accepted\n",
    "n_accepted = outdata_status[outdata_status == 'accepted'].count()\n",
    "\n",
    "# Number of rejected\n",
    "n_rejected = outdata_status[outdata_status == 'rejected'].count()\n",
    "\n",
    "# Total rows\n",
    "total_ppl = outdata_status.count()\n",
    "\n",
    "# Number of accepted divided by the total rows\n",
    "P_accepted = n_accepted/total_ppl\n",
    "\n",
    "# Number of rejected divided by the total rows\n",
    "P_rejected = n_rejected/total_ppl\n",
    "\n",
    "# Group the data by gender and calculate the means of each feature\n",
    "\n",
    "data_means = outdata_full.groupby('status').mean()\n",
    "\n",
    "# View the values\n",
    "\n",
    "print(data_means)\n",
    "\n",
    "# Group the data by gender and calculate the variance of each feature\n",
    "\n",
    "data_variance = outdata_full.groupby('status').var()\n",
    "\n",
    "# View the values\n",
    "\n",
    "print(data_variance)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Means for accepted\n",
    "accepted_loan_amnt_mean = data_means['loan_amnt'][data_variance.index == 'accepted'].values[0]\n",
    "accepted_annual_inc_mean = data_means['annual_inc'][data_variance.index == 'accepted'].values[0]\n",
    "accepted_emp_length_years_mean = data_means['emp_length_years'][data_variance.index == 'accepted'].values[0]\n",
    "\n",
    "\n",
    "# Variance for accepted\n",
    "\n",
    "accepted_loan_amnt_variance = data_variance['loan_amnt'][data_variance.index == 'accepted'].values[0]\n",
    "accepted_annual_inc_variance = data_variance['annual_inc'][data_variance.index == 'accepted'].values[0]\n",
    "accepted_emp_length_years_variance = data_variance['emp_length_years'][data_variance.index == 'accepted'].values[0]\n",
    "\n",
    "# Means for rejected\n",
    "\n",
    "rejected_load_amnt_mean = data_means['loan_amnt'][data_variance.index == 'rejected'].values[0]\n",
    "rejected_annual_inc_mean = data_means['annual_inc'][data_variance.index == 'rejected'].values[0]\n",
    "rejected_emp_length_years_mean = data_means['emp_length_years'][data_variance.index == 'rejected'].values[0]\n",
    "\n",
    "\n",
    "# Variance for rejected\n",
    "\n",
    "rejected_loan_amnt_variance = data_variance['loan_amnt'][data_variance.index == 'rejected'].values[0]\n",
    "rejected_annual_inc_variance = data_variance['annual_inc'][data_variance.index == 'rejected'].values[0]\n",
    "rejected_emp_length_years_variance = data_variance['emp_length_years'][data_variance.index == 'rejected'].values[0]\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Create a function that calculates p(x | y):\n",
    "def p_x_given_y(x, mean_y, variance_y):\n",
    "\n",
    "    # Input the arguments into a probability density function\n",
    "    p = 1/(np.sqrt(2*np.pi*variance_y)) * np.exp((-(x-mean_y)**2)/(2*variance_y))\n",
    "    \n",
    "    # return p\n",
    "    return p\n",
    "\t\n",
    "\n",
    "# Numerator of the posterior if the unclassified observation is a accepted\n",
    "accepted = P_accepted * \\\n",
    "p_x_given_y(person['loan_amnt'][0], accepted_loan_amnt_mean, accepted_loan_amnt_variance) * \\\n",
    "p_x_given_y(person['annual_inc'][0], accepted_annual_inc_mean, accepted_annual_inc_variance) * \\\n",
    "p_x_given_y(person['emp_length_years'][0], accepted_emp_length_years_mean, accepted_emp_length_years_variance)\n",
    "\t\n",
    "# Numerator of the posterior if the unclassified observation is a rejected\n",
    "rejected = P_rejected * \\\n",
    "p_x_given_y(person['loan_amnt'][0], rejected_load_amnt_mean, rejected_loan_amnt_variance) * \\\n",
    "p_x_given_y(person['annual_inc'][0], rejected_annual_inc_mean, rejected_annual_inc_variance) * \\\n",
    "p_x_given_y(person['emp_length_years'][0], rejected_emp_length_years_mean, rejected_emp_length_years_variance)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "print(accepted)\n",
    "print(rejected)\n",
    "\n",
    "#rizik_accepted = 1-accepted*100\n",
    "#rizik_rejected = 1-rejected*100\n",
    "show = \"\"\n",
    "answer1 = \"Transakcija je odobrena\"\n",
    "answer2 = \"Transakcija nije odobrena\"\n",
    "if ( accepted > rejected ) .any():\n",
    "\tprint(answer1)\n",
    "\tshow = answer1\n",
    "#\tprint(\"Stepen rizika {} %procenta\".format(rizik_accepted))\n",
    "else :\n",
    "\tprint(answer2)\n",
    "\tshow = answer2\n",
    "#\tprint(\"Stepen rizika {} %procenta\".format(rizik_rejected))\n",
    "print(show)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Deo koda, koji treba da vrati vrednost show, tj rezultat odluke u receive.html fajl i da ga prikaze."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "\"\"\"\n",
    "@app.route('/receive', methods=['GET', 'POST'])\n",
    "def send():\n",
    "\t\tif request.methods == 'POST':\n",
    "\t\t\treturn render_template('receive.html', showrez=show)\n",
    "\t\t\t\n",
    "if __name__==\"__name__\":\n",
    "\tapp.run()\n",
    "\"\"\""
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
