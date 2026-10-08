# Structured content import

Use child import definitions to import data with a parent–child structure, such as product categories and their
products.

In this example, a saved import definition **ProductCategory** imports product categories. A child definition
then imports the products into the right category.

## Create a child definition

1. In the **Import definitions** tree, open the actions menu of the parent definition (here **ProductCategory**).
2. Select **Create child definition**.

    ![Actions menu of an import definition with Create child definition](../assets/images/structured-content-1.png)

The import wizard starts again, with a few differences described below.

### Select the data source

When you pick the same data source type as the parent, the wizard selects the parent's data source for you.

![Data source step of a child definition, pre-filled with the parent's data source](../assets/images/structured-content-2.png)

### Set the content import options

You don't choose a location, because each item is stored under its parent record. Instead you set the
**parent relation key**: the field that links a record to its parent. In this example that is
`ProductCategoryId`.

![Content import options of a child definition with the parent relation key](../assets/images/structured-content-3.png)

All other steps are the same as in the [import wizard](wizard.md).

## Result

When you run the parent definition, the content tree is filled with the categories and their products.

![Content tree with imported categories and the products below them](../assets/images/structured-content-4.png)

The **Import definitions** tree shows **Products** as a child of **ProductCategory**.

!!! note
    Running a parent definition also runs its child definitions.
